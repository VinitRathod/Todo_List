from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    email = forms.EmailField(max_length = 50)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)