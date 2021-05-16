from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    email = forms.EmailField(max_length = 50)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)

    widgets = {
        'first_name': forms.TextInput(attrs={'class':'fname'}),
        'last_name' : forms.TextInput(attrs={'class':'lname'}),
        'email' : forms.EmailInput(attrs={'class':'email'}),
        'message' : forms.Textarea(attrs={'class':'msg'}),
    }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        widgets = {
            'username' : forms.TextInput(attrs={'class':'ruser'}),
            'email' : forms.EmailInput(attrs={'class':'email'}),
            'password1' : forms.PasswordInput(attrs={'class':'rpassword1'}),
            'password2' : forms.PasswordInput(attrs={'class':'rpassword2'}),
        }