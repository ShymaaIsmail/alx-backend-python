from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    # Explicitly declare email as CharField for validation demo
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'user_id',
            'email',
            'username',
            'first_name',
            'last_name',
            'phone_number',
        ]

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    message_body = serializers.CharField()  # Explicit char field

    # SerializerMethodField to return sender's full name
    sender_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = [
            'message_id',
            'sender',
            'sender_full_name',
            'message_body',
            'sent_at',
        ]

    def get_sender_full_name(self, obj):
        return f"{obj.sender.first_name} {obj.sender.last_name}"

    def validate_message_body(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Message body cannot be empty or whitespace.")
        return value

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    conversation_id = serializers.CharField(read_only=True)  # UUID as char field

    class Meta:
        model = Conversation
        fields = [
            'conversation_id',
            'participants',
            'messages',
            'created_at',
        ]
