from django.db import models
from django import forms
from django.core.urlresolvers import reverse
# Create your models here.
class Contact(models.Model):
    name_text = models.CharField(max_length=150, verbose_name='Name')
    email_text = models.CharField(max_length=200, verbose_name='Email Address')
    subject_text = models.CharField(max_length=200, verbose_name='Subject')
    message_text = models.TextField(verbose_name='Message')

    def __unicode__(self):
        return self.name_text

    def get_absolute_url(self):
        return reverse('sendpage', args=(self.pk,))

class Send(models.Model):
    pub_date = models.DateTimeField('date submitted')
