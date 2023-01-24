from django.db import models

class Locataire(models.Model):
    nom = models.Charfield(max_length=200, null=True)
    prenom = models.Charfield(max_length=200, null=True)
    agent = models.ForeignKey()
    adresse = models.TextField()
    
    
    
    def __str__(self):
        return self.nom
# Create your models here.
