import logging
from datetime import datetime, timedelta
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)
logging.basicConfig(filename='requests.log', level=logging.INFO)

# Track message counts per IP address
message_counts = {}

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_entry = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logger.info(log_entry)

class RestrictAccessByTimeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        current_hour = datetime.now().hour
        # Only allow access between 6 PM (18) and 9 PM (21)
        if not (18 <= current_hour < 21):
            return HttpResponseForbidden("Access to chat is only allowed between 6 PM and 9 PM.")

class OffensiveLanguageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'POST' and request.path.startswith('/api/messages'):
            ip = request.META.get('REMOTE_ADDR')
            now = datetime.now()

            # Initialize or clean old entries
            if ip not in message_counts:
                message_counts[ip] = []
            # Remove messages older than 1 minute
            message_counts[ip] = [ts for ts in message_counts[ip] if now - ts < timedelta(minutes=1)]

            # Check rate limit
            if len(message_counts[ip]) >= 5:
                return HttpResponseForbidden("Rate limit exceeded: Max 5 messages per minute.")

            # Add current timestamp
            message_counts[ip].append(now)

class RolepermissionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/api/messages') and request.method == 'POST':
            user = request.user
            if not user.is_authenticated:
                return HttpResponseForbidden("Authentication required.")
            if not (user.is_superuser or getattr(user, 'role', None) in ['admin', 'moderator']):
                return HttpResponseForbidden("Permission denied: Admin or Moderator required.")
