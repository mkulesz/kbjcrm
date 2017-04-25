from kbjcrm.models import *

class Control:
    def select( year ):
        select = Naleznosc.objects.filter(Data_platnosci__year = year)
        return select

    def generate( number ):

        return 0

    def select_all(_self_):
        select_all = Naleznosc.objects.all()
        return select_all