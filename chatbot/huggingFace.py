# Necessary imports
import fitz  # PyMuPDF
import os
import json
import pandas as pd
from transformers import PreTrainedModel, PretrainedConfig, AutoTokenizer, AutoModel
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from transformers.modeling_outputs import SequenceClassifierOutput
import torch
from dotenv import load_dotenv
from huggingface_hub import HfApi, Repository

# Load environment variables from .env file
load_dotenv()

# Verify if OPENAI_API_KEY is properly loaded
openai_api_key = os.getenv("OPENAI_API_KEY")

# Extract text from PDFs
def extract_text_from_pdf(pdf_path):
    text = ""
    document = fitz.open(pdf_path)
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

# Combine text from CSV and PDFs
def get_csv_text(csv_file_path):
    text = ""
    df = pd.read_csv(csv_file_path)
    for index, row in df.iterrows():
        text += ' '.join(str(value) for value in row.values) + "\n"
    return text

def combine_texts(csv_file_path, pdf_file_paths):
    csv_text = get_csv_text(csv_file_path)
    pdf_texts = [extract_text_from_pdf(pdf) for pdf in pdf_file_paths]
    combined_text = csv_text + "\n".join(pdf_texts)
    return combined_text

# Defining custom model
class CustomConversationalModel(PreTrainedModel):
    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained("hkunlp/instructor-xl")
        self.model = AutoModel.from_pretrained("hkunlp/instructor-xl")
        self.vectorstore = None
        self.conversation_chain = None

    def initialize_conversation_chain(self, combined_text):
        text_chunks = self._get_text_chunks(combined_text)
        self.vectorstore = self._get_vectorstore(text_chunks)
        self.conversation_chain = self._get_conversation_chain(self.vectorstore)

    def _get_text_chunks(self, text):
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
        return chunks

    def _get_vectorstore(self, text_chunks):
        embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
        vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
        return vectorstore

    def _get_conversation_chain(self, vectorstore):
        llm = ChatOpenAI()
        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
        conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vectorstore.as_retriever(), memory=memory)
        return conversation_chain

    def forward(self, input_ids, attention_mask=None, token_type_ids=None, labels=None):
        outputs = self.model(input_ids=input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
        logits = outputs[0]
        loss = None
        if labels is not None:
            loss_fct = torch.nn.CrossEntropyLoss()
            loss = loss_fct(logits.view(-1, self.config.num_labels), labels.view(-1))
        return SequenceClassifierOutput(loss=loss, logits=logits)

    def save_pretrained(self, save_directory):
        super().save_pretrained(save_directory)
        self.tokenizer.save_pretrained(save_directory)
        self.vectorstore.save_local(save_directory)

        # Save embeddings information in a format that can be loaded
        embeddings_info = {
            'model_name': "hkunlp/instructor-xl",
        }
        with open(os.path.join(save_directory, "embeddings_info.json"), 'w') as f:
            json.dump(embeddings_info, f)

    @classmethod
    def from_pretrained(cls, load_directory, *model_args, **kwargs):
        print(f"Loading model from Hugging Face repository")
        model = super().from_pretrained(load_directory, *model_args, config=CustomConfig(), **kwargs)
        print("Model loaded successfully.")

        print("Loading tokenizer...")
        model.tokenizer = AutoTokenizer.from_pretrained(load_directory)
        print("Tokenizer loaded.")
        with open(os.path.join(load_directory, "embeddings_info.json"), 'r') as f:
            embeddings_info = json.load(f)

        print("Loading vectorstore...")
        embeddings = HuggingFaceInstructEmbeddings(model_name=embeddings_info['model_name'])
        model.vectorstore = FAISS.load_local(load_directory, embeddings, allow_dangerous_deserialization=True)
        print("Vectorstore loaded.")
        model.conversation_chain = model._get_conversation_chain(model.vectorstore)

        return model


class CustomConfig(PretrainedConfig):
    model_type = "custom-conversational-model"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


def train_model(csv_file_path, pdf_file_paths, save_directory):
    # Create and initialize the model
    config = CustomConfig()
    model = CustomConversationalModel(config)

    combined_text = combine_texts(csv_file_path, pdf_file_paths)
    model.initialize_conversation_chain(combined_text)

    # Save the model
    model.save_pretrained(save_directory)


def load_pretrained_model(model_directory):
    # Load pretrained model
    model = CustomConversationalModel.from_pretrained(model_directory)
    return model
