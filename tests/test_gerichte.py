import pytest
from mypkg.my_gerichte import Hueftsteak, WienerSchnitzel

def test_hueftsteak():
	assert(Hueftsteak().getPreis() > 0)
	assert(Hueftsteak().druckeBeschreibung() == 'Hueftsteak')

def test_wienerschnitzel():
	assert(WienerSchnitzel().getPreis() > 0)
	assert(WienerSchnitzel().druckeBeschreibung() == 'Wiener Schnitzel')

def test_schnitzel_ist_billiger_als_steak():
	assert(Hueftsteak().getPreis() > WienerSchnitzel().getPreis())
