import json

from django.http import HttpResponse

class JsonResponse(HttpResponse):
    """
    HttpResponse wrapper to return a json-formatted response
    """
    def __init__(self, response):
        return super(JsonResponse, self).__init__(json.dumps(response),
                                                  content_type="application/json")
