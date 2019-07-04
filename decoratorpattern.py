from abc import ABCMeta

@six.add_metaclass(ABCMeta)
class Abstract_Gericht(object):
   def getPreis(self):
      pass
   def druckeBeschreibung(self):
      pass

class Hueftsteak(Abstract_Gericht):
   def getPreis(self):
      return 12.50
   def druckeBeschreibung(self):
      return 'Hueftsteak'

class WienerSchnitzel(Abstract_Gericht):
   def getPreis(self):
      return 7.50
   def druckeBeschreibung(self):
      return 'Wiener Schnitzel'

@six.add_metaclass(ABCMeta)
class Abstract_Gericht_Decorator(Abstract_Gericht):
   def __init__(self,decorated_Gericht):
      self.decorated_gericht = decorated_gericht
   def getPreis(self):
      return self.decorated_gericht.getPreis()
   def druckeBeschreibung(self):
      return self.decorated_gericht.druckeBeschreibung()

class Bratkartoffeln(Abstract_Gericht_Decorator):
   def __init__(self,decorated_gericht):
      Abstract_Gericht_Decorator.__init__(self,decorated_gericht)
   def getPreis(self):
      return self.decorated_gericht.getPreis() + 3.50
   def druckeBeschreibung(self):
	   return self.decorated_gericht.druckeBeschreibung() + ', Bratkartoffeln'

class Salat(Abstract_Gericht_Decorator):
   def __init__(self,decorated_gericht):
      Abstract_Gericht_Decorator.__init__(self,decorated_gericht)
   def getPreis(self):
      return self.decorated_gericht.getPreis() + 2.50
   def druckeBeschreibung(self):
      return self.decorated_gericht.druckeBeschreibung() + ', Salat'

class Suppe(Abstract_Gericht_Decorator):
   def __init__(self,decorated_gericht):
      Abstract_Gericht_Decorator.__init__(self,decorated_gericht)
   def getPreis(self):
      return self.decorated_gericht.getPreis() + 3.00
   def druckeBeschreibung(self):
      return self.decorated_gericht.druckeBeschreibung() + ', Suppe'
