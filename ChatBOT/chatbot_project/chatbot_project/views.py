from rest_framework import generics
from .models import ChatMessage


class ChatMessageListCreate(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessage
