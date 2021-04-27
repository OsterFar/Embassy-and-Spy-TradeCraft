from django import forms
from django.forms import ModelForm
from blog.models import User


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class VisaForm(ModelForm):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'email', 'cnic', 'gender', 'address', 'dob']
