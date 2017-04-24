from kbjcrm.models import Kontrakt

class Control:
    def Select( year ):
        select = Kontrakt.objects.filter(Data_platnosci_fizycznej__year = year)
        return select