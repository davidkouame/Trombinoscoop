'''
Created on Jun 20, 2017

@author: bootnet
'''
from django import forms 

class loginForm(forms.Form):
    email = forms.EmailField(label="Courriel")
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super (loginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        
        
        if any(self.errors):
            return self.errors
    
        #vérifie que les deux champs sont vdalided
        if email and password:
            if password != "test" or email != "test@gmail.com":
                raise forms.ValidationError("Adresse de courriel ou mot de passe erroné")
        
        return cleaned_data  