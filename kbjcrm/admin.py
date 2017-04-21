from django.contrib import admin
#from.models import OsobaKontaktowa
from.models import Osoba
from.models import Kontrahent
from.models import Produkt
from.models import Kontrakt
from.models import Kontrahent_Osoba

# Register your models here.

#admin.site.register(OsobaKontaktowa)
admin.site.register(Osoba)
admin.site.register(Kontrahent)
admin.site.register(Produkt)
admin.site.register(Kontrakt)
admin.site.register(Kontrahent_Osoba)
