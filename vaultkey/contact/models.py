from django.db import models
from django import forms
from django.core.urlresolvers import reverse
# Create your models here.
class Contact(models.Model):
    name_text = models.CharField(max_length=100)
    email_text = models.CharField(max_length=200)
    message_text = models.TextField()
    
    def __unicode__(self):
        return self.name_text

    def get_absolute_url(self):
        return reverse('submitpage', args=(self.pk,))

class Submit(models.Model):
    pub_date = models.DateTimeField('date submitted')
