from django.db import models

class Parraine(models.Model):
  nom = models.CharField(max_length=120)
  prenom = models.CharField(max_length=120)
  numero_electeur = models.CharField(max_length=120, unique=True)
  numero_identification = models.CharField(max_length=120)
  date_naissance = models.CharField(max_length=120)
  lieu_naissance = models.CharField(max_length=120)
  commune = models.CharField(max_length=120)
  departement = models.CharField(max_length=120)
  region = models.CharField(max_length=120, default='')

  def __str__(self):
    return self.nom




class Fichier(models.Model):
  nom = models.CharField(max_length=120)
  prenom = models.CharField(max_length=120)
  numero_electeur = models.CharField(max_length=120, unique=True)
  numero_identification = models.CharField(max_length=120)
  date_naissance = models.CharField(max_length=120)
  lieu_naissance = models.CharField(max_length=120)
  commune = models.CharField(max_length=120)
  departement = models.CharField(max_length=120)
  region = models.CharField(max_length=120, default='')

  def __str__(self):
    return self.nom
