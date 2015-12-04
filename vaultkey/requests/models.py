from django.db import models

# Create your models here.
class Request(models.Model):
    name_text = models.CharField(max_length=100)
    email_text = models.CharField(max_length=100)
    card_name = models.CharField(max_length=150)
    card_quantity = models.IntegerField()
    alter_type = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date submitted')

    def __unicode__(self):
        return self.name_text
