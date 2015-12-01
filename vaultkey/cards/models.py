from django.db import models

class Card(models.Model):
    article_name = models.CharField(max_length=200)

    article_text = models.TextField()

    pub_date = models.DateTimeField('date submitted')

    def __unicode__(self):
        return self.article_name
# Create your models here.
