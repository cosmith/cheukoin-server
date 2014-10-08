from cheukoin.utils import JsonResponse
from cheukoin.models import Lobby

def index(request):
    return JsonResponse({"hello": "test"})

def lobby_new(request):
    lobby = Lobby.objects.create(name="test")
    return JsonResponse({"success": True, "lobby": lobby.to_dict()})

def lobby_list(request):
    lobbies = [l.to_dict() for l in Lobby.objects.all()] or None
    return JsonResponse({"lobbies": lobbies})
