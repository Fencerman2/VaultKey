from django.db import models

class Card(models.Model):
    article_text = models.TextField()

    pub_date = models.DateTimeField('date submitted')
# Create your models here.
