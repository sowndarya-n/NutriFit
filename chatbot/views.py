# chatbot/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .huggingFace import CustomConversationalModel
import os

# Global variables
conversation_chain = None
chat_history = None
model_loading = False  # Flag to track model loading state

# Function to load model
def load_model():
    global conversation_chain, chat_history, model_loading
    model_loading = True
    # Construct absolute path to nutriFitModel_new
    model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nutriFitModel_new')
    
    if os.path.exists(model_dir):
        model = CustomConversationalModel.from_pretrained(model_dir)
        conversation_chain = model.conversation_chain
        chat_history = None
        print("Model loaded successfully.")
    else:
        print(f"Local model directory {model_dir} not found.")
        raise FileNotFoundError(f"Local model directory {model_dir} not found.")
    model_loading = False

# Initialize conversation chain if not already initialized
def initialize_conversation_chain():
    global conversation_chain
    if conversation_chain is None:
        load_model()

# Django view for chatbot
def chatbot_view(request):
    global conversation_chain, chat_history, model_loading

    # Initialize the conversation chain if not already done
    initialize_conversation_chain()

    if request.method == 'POST':
        user_question = request.POST.get('question')
        if model_loading:
            return JsonResponse({'bot_response': "Model is not fully loaded yet, please wait...", 'chat_history': []})
        elif conversation_chain is None:
            return JsonResponse({'bot_response': "Model failed to load, please refresh or try again later.", 'chat_history': []})

        response = conversation_chain({'question': user_question})
        chat_history = response['chat_history']

        # Extract the latest bot response
        bot_response = chat_history[-1].content if chat_history else ""

        # Convert chat history to JSON serializable format
        chat_history_serializable = [{'role': 'user' if i % 2 == 0 else 'bot', 'content': msg.content} for i, msg in enumerate(chat_history)]

        return JsonResponse({'bot_response': bot_response, 'chat_history': chat_history_serializable})

    # Pass model_loading to the template context
    return render(request, 'chatbot/chatbot.html', {'model_loading': model_loading})
