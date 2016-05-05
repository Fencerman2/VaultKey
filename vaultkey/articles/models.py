from django.db import models
from player.models import Player

class Article(models.Model):
    article_name = models.CharField(max_length=200);

    article_text = models.TextField();

    author = models.ForeignKey(Player);

    pub_date = models.DateTimeField('date submitted');

    image = models.FileField();

    def __unicode__(self):
        return self.article_name
# Create your models here.
