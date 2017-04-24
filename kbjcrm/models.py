from django.db import models

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
    Telefon     = models.IntegerField(blank=True, null=True)
    Mail        = models.EmailField(blank=True, null=True)
    Login       = models.CharField(max_length=10, blank=True, null=True)
    Hasło       = models.CharField(max_length=20, blank=True, null=True)
    Rola        = models.ForeignKey(Rola)
    class Meta:
        verbose_name_plural = "Osoba"

    def __str__(self):
        retstr =    str(self.IdOsoba)+' '+self.Imie+' '+self.Nazwisko+' '+self.Mail

        return retstr

class Kontrahent(models.Model):
    IdKontrahent    = models.IntegerField(auto_created=True, primary_key=True, editable=False)
    Nazwa           = models.CharField(max_length=50)
    Opis            = models.TextField(blank=True, null=True)
    Adres           = models.TextField(blank=True, null=True)
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
    RCP                         = models.CharField(max_length=30, default= '')
    class Meta:
        verbose_name_plural = "Kontrakt"

    def __str__(self):
        return self.RCP

class Naleznosc(models.Model):
    IDKonta         = models.ForeignKey(Kontrakt)
    IDNaleznosc     = models.IntegerField(auto_created=True, primary_key=True, editable=False)
    Data_platnosci  = models.DateField()
    Tytul           = models.CharField(max_length=50, null=True, blank=True)
    Kwota_oplaty    = models.IntegerField(default=0)
    Zrealizowane    = models.BooleanField()
    class Meta:
        verbose_name_plural = "Należność"

    def __str__(self):
        return str(self.IDKonta)
