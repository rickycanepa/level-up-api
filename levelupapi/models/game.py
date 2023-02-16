from django.db import models

class Game(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name="game")
    min_player = models.IntegerField()
    max_player = models.IntegerField()