from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """ Custom user model extending Django's AbstractUser. """
    # Extend as needed
    bio = models.TextField(blank=True, null=True)

class Conversation(models.Model):
    """ Model representing a conversation between users. """
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id}"

class Message(models.Model):
    """ Model representing a message in a conversation. """
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    conversation = models.ForeignKey(Conversation,
                                    on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.content[:20]}"
