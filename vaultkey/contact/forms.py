from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name_text', 'email_text', 'subject_text', 'message_text')
