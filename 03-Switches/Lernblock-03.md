## Lernblock 03 - Switches

### Aufgabe 1
#### 1.1
    - Synchronisation, Strukturierung des Datenstroms
    - Medienzugangskontrolle bei geteilten Medien
    - Verfälschungs- und Verlustsicherung
    - Flusssteuerung

#### 1.2
    - Jede Schicht erfüllt spezifische Funktion, kann unabhängig von anderen Schichten implementiert werden -> einfacher und nicht so komplex
    - Komponenten können bei genormten Schnittstellen ausgetauscht werden

#### 1.3
    - Horizontale Kommunikation: innerhalb einer Schicht
    - Vertikale Kommunikation: zwischen 2 Schichten


### Aufgabe 2
#### 2.1
"Bessere" Handhabung der Datenübertragung durch Paketbildung möglich, da
- schnellere Fehlerentdeckung und -behandlung durch "Häppchenweises" übertragen von Daten
- bei kürzeren Datenübertragungen Chance für Fehler geringer 
  -> bei Fehler und erneutem Senden muss nicht gesamte Datenmenge übertragen werden, sondern nur das Datenpaket, in dem Fehler auftaucht
- im Sinne der Flusssteuerung Überlastung des Empfängers zu verhindern
- bei mehreren Netzteilnehmern Chance für andere Netzteilnehmer, schneller zu senden 
  (zB Sender A sendet große Datenmenge, Übertragungsdauer v. 10min, Sender B möchte nach 1min kleine Datenmenge, Übertragungsdauer v. 1min, senden -> müsste 10min abwarten, obwohl Übertragungsdauer viel kürzer wäre -> "besser", wenn nach 1min Chance zur Sendung möglich)

#### 2.2
Abgrenzung einzelner Datenpakete durch 
- Start- bzw. Endflags 
  -> bestimmte Bitfolge, die für Sender und Empfänger bedeutet (Einigung durch gemeinsames Protokoll, zB 01111110), dass Paket zuende ist/ anfängt

Paket ist nach Endflag zuende (Unterscheidung Start-/Endflag danach, ob vorher Startflag kam - erste Flag immer Startflag - oder Endflag)

#### 2.3
Nutzung eines geteilten Mediums von mehreren Nutzern möglich durch:
- Kennzeichnung der Mediennutzung: Nutzer 1 prüft vor Nutzung, ob Medium frei - dann nutzbar - senden, ansonsten warten und nochmals prüfen
- Regelung, wer wann senden darf: Minute 1 darf Nutzer 1 senden, Minute 2 Nutzer 2 usw. bis alle dran waren - Nutzer 1 darf wieder senden, dann Nutzer 2 usw.
- Unterscheidbarkeit unterschiedlicher Sendungen:
Sendung 1 von Nutzer 1 zu Nutzer 3 hat andere Übertragungsfrequenz als Sendung 2 von Nutzer 2 zu Nutzer 4