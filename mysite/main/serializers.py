from rest_framework import serializers

from .models import User, Chat

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ()


class ChatSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Chat
        fields = ('id', 'email', 'text', 'created', 'updated')








# ModelSerializer
# HyperlinkedModelSerializer

