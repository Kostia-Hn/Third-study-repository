import datetime


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        a = datetime.datetime.now()
        response = self.get_response(request)

        b = datetime.datetime.now()
        print('Execution time is ' + str(b - a))
        return response
