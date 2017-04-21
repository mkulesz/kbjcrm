from django.contrib import admin
#from.models import OsobaKontaktowa
from.models import Osoba
from.models import Kontrahent
# Register your models here.

#admin.site.register(OsobaKontaktowa)
admin.site.register(Osoba)
admin.site.register(Kontrahent)

class ItemAdmin(admin.ModelAdmin):
    exclude=("headline ",)

    def get_readonly_fields(self, request, obj=None):
        return ['IdOsoba ']
