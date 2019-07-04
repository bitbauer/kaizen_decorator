import six
from abc import ABCMeta, abstractmethod

@six.add_metaclass(ABCMeta)
class Abstract_Gericht_Component(object):
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


@six.add_metaclass(ABCMeta)
class Abstract_Gericht_Decorator(Abstract_Gericht_Component):
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
