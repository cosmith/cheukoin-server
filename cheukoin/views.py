from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from cheukoin.utils import JsonResponse, JsonResponseError
from cheukoin.models import Lobby

def index(request):
    return JsonResponse({"hello": "test"})

@csrf_exempt
def test(request):
    result = {
        "get": request.GET,
        "post": request.POST
    }
    return JsonResponse(result)


class LobbyCreate(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(LobbyCreate, self).dispatch(*args, **kwargs)

    def post(self, request):
        name = request.POST.get("name")
        if not name:
            return JsonResponseError("You must supply the `name` argument")
        lobby = Lobby.objects.create(name=name)
        return JsonResponse({"success": True, "lobby": lobby.to_dict()})

class LobbyList(View):
    def get(self, request):
        lobbies = [l.to_dict() for l in Lobby.objects.all()] or None
        return JsonResponse({"lobbies": lobbies})
