from django.db import models

class Card(models.Model):
    article_name = models.CharField(max_length=200)

    article_text = models.TextField()

    pub_date = models.DateTimeField('date submitted')
# Create your models here.
