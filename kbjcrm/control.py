from kbjcrm.models import *

class Control:
    def Select( year ):
        select = Naleznosc.objects.filter(Data_platnosci__year = year)
        return select