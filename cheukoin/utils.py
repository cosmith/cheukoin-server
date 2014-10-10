import json

from django.http import HttpResponse

class JsonResponse(HttpResponse):
    """
    HttpResponse wrapper to return a json-formatted response
    """
    def __init__(self, response):
        return super(JsonResponse, self).__init__(
            json.dumps(response, indent=2),
            content_type="application/json"
        )

class JsonResponseError(JsonResponse):
    """
    HttpResponse wrapper to return a json error message
    """
    def __init__(self, message):
        self.status_code = 500
        return super(JsonResponseError, self).__init__({"success": False, "message": message})

