from django.db import models

# Create your models here.
class Player(models.Model):
    player_firstname = models.CharField(max_length=100);
    player_lastname = models.CharField(max_length=100);
    player_description = models.TextField();
    image = models.FileField(blank=True, null=True);

    def __unicode__(self):
        return self.player_firstname + " " + self.player_lastname
