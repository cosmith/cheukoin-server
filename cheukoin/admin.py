from django.contrib import admin
from cheukoin.models import Lobby

class LobbyAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Lobby, LobbyAdmin)
