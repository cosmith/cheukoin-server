from cheukoin.utils import JsonResponse


def index(request):
    return JsonResponse({"Hello": "test"})
