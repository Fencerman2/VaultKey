from django.db import models
from django import forms
from django.core.urlresolvers import reverse
# Create your models here.
class Request(models.Model):
    name_text = models.CharField(max_length=100, verbose_name='Name')
    email_text = models.CharField(max_length=100, verbose_name='Email Address')
    card_name = models.CharField(max_length=150, verbose_name='Card Name')
    card_set = models.CharField(max_length=150, verbose_name='Card Set')
    card_quantity = models.IntegerField()
    alter_type = models.CharField(max_length=30, verbose_name='Alter Type',
        choices=(("FLessBasic","Frameless Basic Land ($7)"),
        ("Part","Partial/Pop Up ($15)"),
        ("FABasic","Full Art Basic Land Extension ($15)"),
        ("FrLess","Frameless ($20)"),
        ("FrLessSwapSimp","Frameless Art Swap - Simple ($30)"),
        ("FrLessSwapComp","Frameless Art Swap - Complex ($40)"),
        ("FA","Full Art Extension ($35)"),
        ("Custom","Custom Full Art Swap ($45+)")))
    card_provided = models.BooleanField()

    def __unicode__(self):
        return self.name_text

    def get_absolute_url(self):
        return reverse('submitpage', args=(self.pk,))

class Submit(models.Model):
    pub_date = models.DateTimeField('date submitted')
