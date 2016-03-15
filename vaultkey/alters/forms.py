from django import forms
from .models import Request
class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('name_text', 'email_text', 'card_name', 'card_set', 'card_quantity',
            'alter_type', 'card_provided')
