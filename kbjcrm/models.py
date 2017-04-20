from django.db import models

# Create your models here.

class OsobaKontaktowa(models.Model):
    pesel       = models.CharField(max_length=11, primary_key=True, )
    imie        = models.CharField(max_length=15)
    nazwisko    = models.CharField(max_length=20)

    def __str__(self):
        rv_value = self.pesel + self.imie + self.nazwisko
        return rv_value