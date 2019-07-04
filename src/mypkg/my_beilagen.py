from abstract_gericht import Abstract_Gericht_Decorator

class Bratkartoffeln(Abstract_Gericht_Decorator):
    def getPreis(self):
        return self._component.getPreis() + 3.50
    def druckeBeschreibung(self):
        return self._component.druckeBeschreibung() + ', Bratkartoffeln'

class Salat(Abstract_Gericht_Decorator):
    def getPreis(self):
        return self._component.getPreis() + 2.50
    def druckeBeschreibung(self):
        return self._component.druckeBeschreibung() + ', Salat'

class Suppe(Abstract_Gericht_Decorator):
    def getPreis(self):
        return self._component.getPreis() + 3.00
    def druckeBeschreibung(self):
        return self._component.druckeBeschreibung() + ', Suppe'
