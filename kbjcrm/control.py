from kbjcrm.models import Kontrakt

class Control:
    select = Kontrakt.objects.filter(Data_platnosci_fizycznej__year = 2017)