from abstract_gericht import Abstract_Gericht_Component

class Hueftsteak(Abstract_Gericht_Component):
    def getPreis(self):
        return 12.50
    def druckeBeschreibung(self):
        return 'Hueftsteak'

class WienerSchnitzel(Abstract_Gericht_Component):
    def getPreis(self):
        return 7.50
    def druckeBeschreibung(self):
        return 'Wiener Schnitzel'
