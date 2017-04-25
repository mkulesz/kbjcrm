from kbjcrm.models import *
from datetime import *

class Control:
    def select( year ):
        select = Naleznosc.objects.filter(Data_platnosci__year = year)
        return select

    def generate( number, idrcp ):


        rcp = Naleznosc.objects.filter(IDKontrakt=idrcp)
        RCP = Naleznosc()
        RCP.IDKonttrakt = rcp
        startdate = rcp.Data_platnosci
        RCP.Data_platnosci = date(year=int(number), month=startdate.month, day=startdate.day)
        RCP.Tytul = rcp.Tytul + ' ' + str(RCP.Data_platnosci)
        RCP.Kwota_oplaty = rcp.Kwota_oplaty
        RCP.Zrealizowane = rcp.Zrealizowane
        RCP.save()

        return 0

    def select_all(_self_):
        select_all = Produkt.objects.all()
        return select_all
