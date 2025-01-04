import logging

#filter which is searching for IPs
class RequestFilter(logging.Filter):
    def filter(self, record):
        request = getattr(record, 'request', None)
        if request and hasattr(request, 'META'):
            record.ip = request.META.get('REMOTE_ADDR', 'unknown')
        else:
            record.ip = 'no_request'
        return True
