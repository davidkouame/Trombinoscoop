'''
Created on Jun 20, 2017

@author: bootnet
'''
from django.db import models
from django.utils import timezone

class Personne(models.Model):
    matricule = models.CharField(max_length=10)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_de_naissance = models.DateField()
    email = models.EmailField()
    tel_fixe = models.CharField(max_length=20)
    mot_de_passe = models.CharField(max_length=32)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
