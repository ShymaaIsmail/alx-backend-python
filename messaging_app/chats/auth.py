from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

def get_tokens_for_user(user):
    """
    Generates refresh and access tokens for the given user.
    """
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def authenticate_user(email, password):
    """
    Custom authentication logic (optional override).
    """
    user = authenticate(username=email, password=password)
    return user
