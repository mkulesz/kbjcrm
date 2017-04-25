from kbjcrm.models import *
from datetime import *


class Control:
    def select(year):
        select = Naleznosc.objects.filter(Data_platnosci__year=year)
        return select

    def generate(number, idrcp):
        for rcp in Kontrakt.objects.filter(Produkt__Nazwa=idrcp):
            naleznosc = Naleznosc.objects.get(IDKontrakt=rcp)
            RCP = Naleznosc()
            RCP.IDKonttrakt = naleznosc
            startdate = naleznosc.Data_platnosci
            RCP.Data_platnosci = date(year=int(number), month=startdate.month, day=startdate.day)
            RCP.Tytul = naleznosc.Tytul + ' ' + str(RCP.Data_platnosci)
            RCP.Kwota_oplaty = naleznosc.Kwota_oplaty
            # RCP.Zrealizowane = naleznosc.Zrealizowane
            Naleznosc.objects.create()

        return 0

    def select_all(_self_):
        select_all = Produkt.objects.all()
        return select_all
