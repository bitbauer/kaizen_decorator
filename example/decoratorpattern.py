from abc import ABCMeta, abstractmethod

class Abstract_Gericht_Component(ABCMeta):
    """
    Define the interface for objects that can have responsibilities
    added to them dynamically.
    """
    @abstractmethod
    def getPreis(self):
        pass
    @abstractmethod
    def druckeBeschreibung(self):
        pass

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

class Abstract_Gericht_Decorator(Abstract_Gericht_Component, ABCMeta):
    """
    Maintain a reference to a Component object and define an interface
    that conforms to Component's interface.
    """
    def __init__(self,component):
        self._component = component
    @abstractmethod
    def getPreis(self):
        pass
    @abstractmethod
    def druckeBeschreibung(self):
        pass

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
