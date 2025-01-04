import logging

'''
class RequestFilter(logging.Filter):
    def filter(self, record):
        try:
            from django.utils.log import RequestLogRecord
            request = getattr(record, 'request', None)
            if request:
                record.ip = request.META.get('REMOTE_ADDR', 'unknown')  # taking IP
            else:
                record.ip = 'no_request'
        except Exception as e:
            record.ip = 'error'
        return True '''

class RequestFilter(logging.Filter):
    def filter(self, record):
        request = getattr(record, 'request', None)
        if request:
            record.ip = request.META.get('REMOTE_ADDR', 'unknown')
        else:
            record.ip = 'no_request'
        return True