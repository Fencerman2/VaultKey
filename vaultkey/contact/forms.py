from django import forms
from .models import Contact
class RequestForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name_text', 'email_text', 'message_text')
