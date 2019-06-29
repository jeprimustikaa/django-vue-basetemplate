from django.http import HttpResponse
from django.views import View

class IndexView(View):
    """
    Index homepage view
    """
    message = "Hello World!"
    def get(self, request):
        return HttpResponse(self.message)
