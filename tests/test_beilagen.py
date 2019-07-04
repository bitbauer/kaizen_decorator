
import pytest
from mypkg.my_gerichte import Hueftsteak, WienerSchnitzel
from mypkg.my_beilagen import Bratkartoffeln, Salat, Suppe

def test_schnitzel_mit_bratkartoffeln():
	assert(Bratkartoffeln(WienerSchnitzel()).getPreis() > WienerSchnitzel().getPreis())
	assert(Bratkartoffeln(WienerSchnitzel()).druckeBeschreibung() == 'Wiener Schnitzel, Bratkartoffeln')

def test_hueftsteak_mit_bratkartoffeln_und_salat():
	assert(Salat(Bratkartoffeln(Hueftsteak())).getPreis() > Bratkartoffeln(Hueftsteak()).getPreis())
	assert(Salat(Bratkartoffeln(Hueftsteak())).druckeBeschreibung() == 'Hueftsteak, Bratkartoffeln, Salat')

def test_schnitzel_mit_bratkartoffeln_und_suppe():
	assert(Suppe(Bratkartoffeln(WienerSchnitzel())).getPreis() > Bratkartoffeln(WienerSchnitzel()).getPreis())
	assert(Suppe(Bratkartoffeln(WienerSchnitzel())).druckeBeschreibung() == 'Wiener Schnitzel, Bratkartoffeln, Suppe')
