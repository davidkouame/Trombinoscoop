'''
Created on Jun 19, 2017

@author: bootnet
'''
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import loginForm
def welcome(request):
    return render(request, 'Trombinoscoop/index.html', {'name': "KOUAME"})

def login(request):
    # Test si formulaire a été envoyé
    if request.method == "POST":
        if 'email' not in request.POST or 'password' not in request.POST:
            error = "Veuillez entrez une adresse de courriel et un mot de passe"
            return render(request, 'Trombinoscoop/login.html', {"error", error})
        else:
            email = request.POST["email"]
            password = request.POST["password"]
            
            #teste si le mot de passe et l'email est le bon
            if password != 'test' or email != "test@gmail.com":
                error = "Adresse de courriel électronique ou de mot passe est érroné"
                return render(request, "Trombinoscoop/login.html", {"error": error})
            #tout est bon on va à la page d'acceuil
            else:
                return HttpResponseRedirect('/welcome')
    #test si le formulaire n'a pas été envoyé
    else:
        return render(request, 'Trombinoscoop/login.html')