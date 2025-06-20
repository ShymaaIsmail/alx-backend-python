from rest_framework.permissions import BasePermission

class IsParticipantOfConversation(BasePermission):
    """
    Allows access only to participants of the conversation.
    Applied to both Conversations and Messages.
    """

    def has_object_permission(self, request, view, obj):
        # If the object is a Message, check the conversation
        if hasattr(obj, 'conversation'):
            conversation = obj.conversation
        else:
            conversation = obj  # it's a Conversation

        return request.user in conversation.participants.all()

    def has_permission(self, request, view):
        # Ensure the user is authenticated (should be globally enforced too)
        return request.user and request.user.is_authenticated
