from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=254, label='Utilisateur', widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Identifiant'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput({'class': 'form-control', 'placeholder':'Mot de passe'}))
