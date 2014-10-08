from django.db import models


class Lobby(models.Model):
    name = models.CharField(max_length=200)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
