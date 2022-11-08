#Automatically extracted from ./04_zusammengesetzte-daten.md on 2022-10-25 11:29:58.359987 UTC



#------------------------------------------
#Datendefinition für zusammengesetzte Daten
#------------------------------------------

#[./04_zusammengesetzte-daten.md:50]
# Ein Computer besteht aus:
# - Prozessor
# - Festplatten-Kapazität in Gigabyte
# - Hauptspeicher-Kapazität in Gigabyte



#------------------------------------------
#Modellierung in unserer Programmiersprache
#------------------------------------------

#[./04_zusammengesetzte-daten.md:80]
from wypp import *

@record
class Computer:
    prozessor: str
    festplatte: int
    hauptspeicher: int



#----------------------------
#Kopf der Konstruktorfunktion
#----------------------------

#[./04_zusammengesetzte-daten.md:112]
# def Computer(prozessor: str, festplatte: int, hauptspeicher: int) -> Computer



#---------------------------------------
#Zugriff auf Eigenschaften eines Records
#---------------------------------------

#[./04_zusammengesetzte-daten.md:144]
# c.prozessor    : str
# c.festplatte   : int
# c.hauptspeicher: int



#--------------------
#Arbeiten mit Records
#--------------------

#[./04_zusammengesetzte-daten.md:157]
# Gesamtspeicher berechnen
# Eingabe: ein Computer
# Ergebnis: die Summe von Haupt- und Festplattenspeicher (int)
def totalMemory(c: Computer) -> int:
    pass



#---------
#Der Rumpf
#---------

#[./04_zusammengesetzte-daten.md:192]
def totalMemory(c):
    return c.festplatte + c.hauptspeicher



#------------------------------------
#Funktionen die Records zurückliefern
#------------------------------------

#[./04_zusammengesetzte-daten.md:210]
# Computer für Modell zusammenstellen.



#------------
#Datenanalyse
#------------

#[./04_zusammengesetzte-daten.md:223]
# Ein Modell ist eins der folgenden:
# - Billigmodell
# - Gamer-Modell
# - Office-Modell
Modell = Literal['billig', 'gamer', 'office']



#-----------------------
#Funktionskopf und Tests
#-----------------------

#[./04_zusammengesetzte-daten.md:233]
# Computer für ein bestimmtes Modell zusammenstellen.
# Eingabe: ein Modell
# Ergebnis: ein Computer
def standardComputer(modell: Modell) -> Computer:
    pass



#-------
#Fertig!
#-------

#[./04_zusammengesetzte-daten.md:298]
def standardComputer(modell):
    if modell == 'billig':
        return Computer('Sempron', 2, 500)
    elif modell == 'gamer':
        return Computer('Quad', 16, 1000)
    elif modell == 'office':
        return Computer('Intel i7', 8, 750)



#--------------------------------------
#Datendefinition zusammengesetzte Daten
#--------------------------------------

#[./04_zusammengesetzte-daten.md:320]
# Ein X hat / besteht aus / ist charakterisiert durch:
# - Bestandteil / Eigenschaft 1
# - Bestandteil / Eigenschaft 2
# ...
# - Bestandteil / Eigenschaft n


#[./04_zusammengesetzte-daten.md:330]
# Ein Computer besteht aus:
# - Prozessor
# - Festplatten-Kapazität in Gigabyte
# - Hauptspeicher-Kapazität in Gigabyte



#--------------------------------------
#Fortsetzung der Konstruktionsanleitung
#--------------------------------------

#[./04_zusammengesetzte-daten.md:365]
@record
class Computer:
    prozessor: str
    festplatte: int
    hauptspeicher: int



#------------------------------------
#Typen für Konstruktor und Selektoren
#------------------------------------

#[./04_zusammengesetzte-daten.md:382]
# Konstruktor:
# def T(s1: T1, s2: T2, ..., sn: Tn) -> T
#
# Für einen Wert r des Records T gibt es folgende Selektoren
# r.s1 : T1
# r.s2 : T2
# ...
# r.sn : Tn



#-----------
#Gürteltiere
#-----------

#[./04_zusammengesetzte-daten.md:473]
# Gürteltier nach der Fütterung



#------------
#Datenanalyse
#------------

#[./04_zusammengesetzte-daten.md:479]
# Eingabe: ein Gürteltier und die Menge an Futter in Gramm (int).
# Ergebnis: das Gürteltier nach der Fütterung.



#--------------------------------------------
#Datendefinition und Typdefinition für Status
#--------------------------------------------

#[./04_zusammengesetzte-daten.md:495]
# Ein Status ist eins der folgenden:
# - 'tot'
# - 'lebendig'
Status = Literal['tot', 'lebendig']



#----------------------------------------------------
#Datendefinition und Record-Definition für Gürteltier
#----------------------------------------------------

#[./04_zusammengesetzte-daten.md:504]
# Ein Gürteltier ist charakterisiert durch
# - sein Gewicht in Gramm (int)
# - seinen Status tot oder lebendig
@record
class Gürteltier:
    gewicht: int
    totOderLebendig: Status


#[./04_zusammengesetzte-daten.md:516]
dora = Gürteltier(25000, 'lebendig')
daniel = Gürteltier(30000, 'tot')



#-----------------------
#Funktionskopf und Tests
#-----------------------

#[./04_zusammengesetzte-daten.md:523]
# Gürteltier nach der Fütterung
# Eingabe: ein Gürteltier und die Menge an Futter in Gramm (int).
# Ergebnis: das Gürteltier nach der Fütterung.
def füttereGürteltier(dillo: Gürteltier, foodWeight: int) -> Gürteltier:
    pass



#---------------------------
#Schablonen, vierter Streich
#---------------------------

#[./04_zusammengesetzte-daten.md:598]
# Gürteltier nach der Fütterung
# Eingabe: ein Gürteltier und die Menge an Futter in Gramm (int).
# Ergebnis: das Gürteltier nach der Fütterung.
def füttereGürteltier(dillo: Gürteltier, foodWeight: int) -> Gürteltier:
    if dillo.totOderLebendig == 'tot':
       return dillo
    else:
       return Gürteltier(
           dillo.gewicht + foodWeight // 2,
           dillo.totOderLebendig
       )



#--------------------
#Arbeiten mit Records
#--------------------

#[./04_zusammengesetzte-daten.md:167]
check(totalMemory(Computer('Intel i9', 1000, 16)), 1016)
check(totalMemory(Computer('AMD', 250, 8)), 258)



#-----------------------
#Funktionskopf und Tests
#-----------------------

#[./04_zusammengesetzte-daten.md:241]
check(standardComputer('billig'), Computer('Sempron', 2, 500))
check(standardComputer('gamer'), Computer('Quad', 16, 1000))
check(standardComputer('office'), Computer('Intel i7', 8, 750))


#[./04_zusammengesetzte-daten.md:533]
check(füttereGürteltier(dora, 2000), Gürteltier(26000, 'lebendig'))
check(füttereGürteltier(daniel, 1000), Gürteltier(30000, 'tot'))

