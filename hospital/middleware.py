from django.http import HttpResponseServerError
from django.template.response import TemplateResponse
from django.db.models.deletion import ProtectedError


class ExceptionMiddleware(object):
    """
    Middleware that makes sure clients see a meaningful error message wrapped in a Json response.
    """    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if type(exception) == ProtectedError:
            return TemplateResponse(request, "protected_error.html")
        return HttpResponseServerError()
