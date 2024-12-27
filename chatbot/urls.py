from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot_view, name='chatbot'),  # This maps the root URL to your chatbot view
]
