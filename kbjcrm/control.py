from kbjcrm.models import *
from datetime import *

class Control:
    def select( year ):
        select = Naleznosc.objects.filter(Data_platnosci__year = year)
        return select

    def generate( number, idrcp ):
        rcp = Naleznosc.objects.filter(IDKonta=idrcp)
        RCP = Naleznosc()
        RCP.IDKonta = idrcp
        StartDate = rcp.Data_platnosci
        RCP.Data_platnosci = StartDate.replace(StartDate.year + 1)
        RCP.Tytul = rcp.Tytul + ' ' + str(RCP.Data_platnosci)
        RCP.Kwota_oplaty = rcp.Kwota_oplaty
        RCP.Zrealizowane = rcp.Zrealizowane
        RCP.save()

        return 0

    def select_all(_self_):
        select_all = Naleznosc.objects.all()
        return select_all