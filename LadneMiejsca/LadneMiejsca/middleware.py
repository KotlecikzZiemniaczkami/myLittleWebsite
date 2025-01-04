import logging

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger = logging.getLogger('django')
        logger.setFilter(RequestFilter())

        response = self.get_response(request)
        return response