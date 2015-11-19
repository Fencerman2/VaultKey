from django.db import models

class Cards(models.Model):
    article_text = models.CharField(max_length=10000)

    pub_date = models.DateTimeField('date submitted')
# Create your models here.
