from django import forms
from .models import Request
class RequestForm(forms.ModelForm):
    # name_text = forms.CharField(max_length=100)
    # email_text = forms.CharField(max_length=100)
    # card_name = forms.CharField(max_length=150)
    # card_quantity = forms.IntegerField()
    # alter_type = forms.ChoiceField(choices=["Frameless Basic Land ($7)",
    #     "Partial/Pop Up ($15)","Full Art Basic Land Extension ($15)",
    #     "Frameless($20)","Frameless Art Swap - Simple ($30)",
    #     "Frameless Art Swap - Complex ($40)", "Full Art Extension ($35)",
    #     "Custom Full Art Swap ($45+)"])
    # card_provided = forms.CheckboxInput()

    class Meta:
        model = Request
        fields = ('name_text', 'email_text', 'card_name', 'card_set', 'card_quantity',
            'alter_type', 'card_provided')
