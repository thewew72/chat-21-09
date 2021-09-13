from django.shortcuts import render

from rest_framework import viewsets
from .serializers import UserSerializer, ChatSerializer
from .models import User, Chat


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

