from django import forms

class RequestForm(forms.form)
    name_text = models.CharField(max_length=100)
    email_text = models.CharField(max_length=100)
    card_name = models.CharField(max_length=150)
    card_quantity = models.IntegerField()
    alter_type = models.ChoiceField(choices=["Frameless Basic Land ($7)",
        "Partial/Pop Up ($15)","Full Art Basic Land Extension ($15)",
        "Frameless($20)","Frameless Art Swap - Simple ($30)",
        "Frameless Art Swap - Complex ($40)", "Full Art Extension ($35)",
        "Custom Full Art Swap ($45+)"])
    card_provided = models.CheckboxInput()
