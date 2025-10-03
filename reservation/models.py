from django.db import models

# Create your models here.
class Reservation(models.Model):
    nom_client = models.CharField(max_length=100)
    numero_train = models.CharField()
    carte_transport = models.CharField(default=False)
    date_reservation = models.DateField()
    nombre_personnes = models.IntegerField()

    def __str__(self):
        return f"Réservation de {self.nom_client} pour {self.nombre_personnes} personnes le {self.date_reservation}"