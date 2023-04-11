from django import forms

class CreateNewUserForm(forms.Form):
    nombre= forms.CharField(max_length=20)
    apellido= forms.CharField(max_length=20)
    email=forms.CharField(max_length=25)
    contrasenia=forms.CharField(max_length=12)
    
class LoginForm(forms.Form):
    email=forms.CharField(max_length=25)
    contrasenia=forms.CharField(max_length=12)