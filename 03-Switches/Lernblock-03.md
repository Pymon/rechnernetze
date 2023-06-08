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


### Aufgabe 3
#### 3.1
    MAC-Adressen (Media Access Control) sind eindeutige Kennungen, die Netzwerkgeräten auf der Data Link Layer des OSI-Modells zugewiesen werden. Sie bestehen aus 48 Bit und werden normalerweise in hexadezimaler Form dargestellt. MAC-Adressen werden benötigt, um Geräte in einem Netzwerk zu identifizieren und den Datenverkehr an das richtige Ziel zu senden. Jedes Netzwerkgerät hat eine eindeutige MAC-Adresse, die von seinem Hersteller zugewiesen wird.

#### 3.2
    Bei Ethernet wird der Zugriff auf das Übertragungsmedium durch CSMA/CD (Carrier Sense Multiple Access with Collision Detection) gehandhabt. CSMA/CD ist ein Zugriffsverfahren, bei dem ein Gerät das Medium überwacht, um festzustellen, ob es von anderen Geräten verwendet wird. Wenn das Medium frei ist, sendet das Gerät seine Daten. Wenn jedoch zwei Geräte gleichzeitig Daten senden und eine Kollision auftritt, erkennen die Geräte die Kollision und stoppen die Übertragung. Anschließend warten sie eine zufällige Zeit, bevor sie erneut versuchen, die Daten zu senden.

#### 3.3
    Der Ethernet-Standard gibt eine minimale Größe für Pakete vor, um sicherzustellen, dass das Übertragungsmedium für ausreichend lange Zeit belegt ist, um Kollisionen zu erkennen. Die minimale Paketgröße beträgt 64 Bytes, einschließlich des Preambles und des Start of Frame Delimiters (SFD).
    
#### 3.4
    Der Header eines Ethernet II-Frames besteht aus den folgenden Feldern:
    - Destination MAC Address: Die MAC-Adresse des Zielgeräts.
    - Source MAC Address: Die MAC-Adresse des sendenden Geräts.
    - EtherType: Identifiziert den verwendeten Protokolltyp im Payload des Frames, z.B. IPv4 oder ARP.
    - Optional: Es können optionale Felder wie VLAN-Tags hinzugefügt werden, um spezielle Funktionen zu unterstützen.
    Diese Felder dienen dazu, das Frame durch das Netzwerk zu leiten und sicherzustellen, dass es an das richtige Zielgerät gesendet wird.

#### 3.5
    Um eine Nachricht an alle erreichbaren Rechner in einem lokalen Netzwerk zu senden, wird die spezielle MAC-Adresse "Broadcast MAC Address" verwendet. Diese Adresse hat den Wert "FF:FF:FF:FF:FF:FF". Wenn ein Gerät eine Nachricht mit dieser Adresse als Ziel sendet, werden alle Geräte im Netzwerk diese Nachricht empfangen. Dies ermöglicht es, Informationen an alle Teilnehmer des Netzwerks zu senden.
