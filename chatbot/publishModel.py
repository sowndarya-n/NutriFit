# Necessary imports
import fitz  # PyMuPDF
import os
import json
import pandas as pd
import shutil
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
from huggingface_hub import HfApi, Repository, HfFolder

# Log in to Hugging Face
HfFolder.save_token("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") 

# Initializing the repository
repo_name = "NutriFitWebApp"  
username = "Sonu-31"  

# Creating repository on Hugging Face
api = HfApi()
api.create_repo(repo_id=f"{username}/{repo_name}")

# Clone the repository to a new folder
repo = Repository(local_dir="nutriFitModel_new", clone_from=f"{username}/{repo_name}")

# Move existing files to the new repository folder using shutil
for filename in os.listdir('./nutriFitModel'):
    shutil.move(os.path.join('./nutriFitModel', filename), './nutriFitModel_new/')

# Add and commit the files in the new repository folder
repo.git_add()
repo.git_commit("Initial commit")
repo.git_push()