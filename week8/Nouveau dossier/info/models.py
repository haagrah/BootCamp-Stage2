from django.db import models  

 
class Locataire(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    age = models.IntegerField()
    adresse = models.TextField()
    
    
    
    def __str__(self):
        return self.nom
# Create your models here.
