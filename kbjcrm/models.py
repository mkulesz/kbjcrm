from django.db import models
from django import forms

# Create your models here.
'''
class OsobaKontaktowa(models.Model):
    pesel       = models.CharField(max_length=11, primary_key=True, )
    imie        = models.CharField(max_length=15)
    nazwisko    = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Osoba Kontaktowa"

    def __str__(self):
        rv_value = self.pesel + self.imie + self.nazwisko
        return rv_value
'''
class Osoba(models.Model):
    IdOsoba     = models.IntegerField(auto_created=True, primary_key=True, editable=False)
    Imie        = models.CharField(max_length=20)
    Nazwisko    = models.CharField(max_length=40)
    Telefon     = models.IntegerField()
    Mail        = models.EmailField()
    Login       = models.CharField(max_length=10)
    Hasło       = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = "Osoba"



class Kontrahent(models.Model):
    IdKontrahent    = models.IntegerField(auto_created=True, primary_key=True, editable=False)
    Nazwa           = models.CharField(max_length=50)
    Opis            = models.TextField()
    Adres           = models.TextField()
    NIP             = models.IntegerField()
    Regon           = models.CharField(max_length=10)
    class Meta:
        verbose_name_plural = "Kontrahent"




