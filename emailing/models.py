from email import message
from turtle import mode
from django.db import models

# Create your models here.

class Emailing(models.Model):
    nom = models.CharField(max_length=255, verbose_name="Nom de l'utilisateur")
    mail = models.EmailField(verbose_name="Adresse email", max_length=100)
    sujet = models.CharField(verbose_name="Sujet du mail", max_length=100)
    message = models.TextField()

    def __str__(self):
        return "{}, {}, {}, {}".format(self.nom, self.mail, self.sujet, self.message)