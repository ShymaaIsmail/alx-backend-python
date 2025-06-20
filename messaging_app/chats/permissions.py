from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allows access only to participants of the conversation.
    Applied to both Conversations and Messages.
    """

    def has_object_permission(self, request, view, obj):
        # If it's a Message, check its related conversation
        if hasattr(obj, 'conversation'):
            conversation = obj.conversation
        else:
            conversation = obj  # it's already a Conversation

        return request.user in conversation.participants.all()

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
