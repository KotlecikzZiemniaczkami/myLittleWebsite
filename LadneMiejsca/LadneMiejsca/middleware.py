import logging
from .filters import RequestFilter

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger = logging.getLogger('django')
        logger.addFilter(RequestFilter())
        logger.info(f"New request to {request.path} from IP: {request.META.get('REMOTE_ADDR', 'unknown')}")
        response = self.get_response(request)
        return response