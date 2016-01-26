from django.db import models

# Create your models here.
class Player(models.Model):
    player_name = models.CharField(max_length=100);
    player_description = models.TextField();

    def __unicode__(self):
        return self.player_name
