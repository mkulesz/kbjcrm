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

class Rola(models.Model):
    Rola    = models.CharField(max_length=30, primary_key=True, null=False)
    class Meta:
        verbose_name_plural= "Rola"

    def __str__(self):
        return self.Rola

class Osoba(models.Model):
    IdOsoba     = models.IntegerField(auto_created=True, primary_key=True, editable=False)
    Imie        = models.CharField(max_length=20)
    Nazwisko    = models.CharField(max_length=40)
    Telefon     = models.IntegerField(blank=True)
    Mail        = models.EmailField(blank=True)
    Login       = models.CharField(max_length=10, blank=True)
    Hasło       = models.CharField(max_length=20, blank=True)
    Rola        = models.ForeignKey(Rola)
    class Meta:
        verbose_name_plural = "Osoba"

    def __str__(self):
        retstr =    str(self.IdOsoba)+' '+self.Imie+' '+self.Nazwisko+' '+self.Mail

        return retstr

class Kontrahent(models.Model):
    IdKontrahent    = models.IntegerField(auto_created=True, primary_key=True, editable=False)
    Nazwa           = models.CharField(max_length=50)
    Opis            = models.TextField(blank=True)
    Adres           = models.TextField(blank=True)
    NIP             = models.IntegerField()
    Regon           = models.CharField(max_length=10, blank=True)
    class Meta:
        verbose_name_plural = "Kontrahent"

    def __str__(self):
        return self.Nazwa

class Kontrahent_Osoba(models.Model):
    IdOsoba         = models.ForeignKey(Osoba)
    IdKontrahent    = models.ForeignKey(Kontrahent)
    class Meta:
        verbose_name_plural = "Kontrahent-Osoba"

class Produkt(models.Model):
    IdProduktu      = models.IntegerField(auto_created=True, primary_key=True, editable=False)
    Nazwa           = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Produkt"

    def __str__(self):
        return self.Nazwa

class Kontrakt(models.Model):
    Nr                          = models.IntegerField(auto_created=True, primary_key=True, editable=False)
    Data_zawarcia               = models.DateField()
    Kontrahent                  = models.ForeignKey(Kontrahent)
    Produkt                     = models.ForeignKey(Produkt)
    Data_platnosci_fizycznej    = models.DateField()
    Kwota_oplaty_licencyjnej    = models.IntegerField(default=0)
    RCP                         = models.CharField(max_length=30, default= '')
    class Meta:
        verbose_name_plural = "Kontrakt"

    def __str__(self):
        return self.Nr
