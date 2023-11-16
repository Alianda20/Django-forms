from django import forms

class Studentforms(forms.Form):
    fname=forms.CharField(label="Your first name",max_length=30)
    lname=forms.CharField(label="Your last name",max_length=30)
    email=forms.EmailField(label="Your email", max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())