import logging
from datetime import datetime, timedelta
from django.http import HttpResponseForbidden

# Set up basic logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename='requests.log', level=logging.INFO)

# For tracking message limits
message_log = {}


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        # Restrict access outside 6PM to 9PM
        if not (18 <= current_hour < 21):
            return HttpResponseForbidden("Access restricted: Allowed only between 6PM and 9PM.")
        return self.get_response(request)


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' and request.path.startswith('/api/messages'):
            ip = request.META.get('REMOTE_ADDR')
            now = datetime.now()
            timestamps = message_log.get(ip, [])
            timestamps = [ts for ts in timestamps if now - ts < timedelta(minutes=1)]
            if len(timestamps) >= 5:
                return HttpResponseForbidden("Rate limit exceeded: 5 messages per minute allowed.")
            timestamps.append(now)
            message_log[ip] = timestamps
        return self.get_response(request)


class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/messages') and request.method == 'POST':
            user = request.user
            if not user.is_authenticated:
                return HttpResponseForbidden("Authentication required.")
            if not (user.is_superuser or getattr(user, 'role', None) in ['admin', 'moderator']):
                return HttpResponseForbidden("Permission denied: Admin or Moderator required.")
        return self.get_response(request)
