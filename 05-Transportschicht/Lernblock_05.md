## Lernblock 5 Transportschicht

### Aufgabe 1
Zur Adressierung auf der Transportschicht werden Ports verwendet, zur Kommunikation zwischen unterschiedlichen Anwendungen eines Rechners mit unterschiedlichen Anwendungen eines anderen Rechners

### Aufgabe 2
Sockets bestehen aus Internetadresse und einem Port, beschreibt die Gesemtheit aus IP-Adresse und der "Prozess-Adresse"

### Aufgabe 3
Port 80 wird standardmäßig von einem Webbrowser für  HTTP-Requests an einen Webserver verwendet

### Aufgabe 4 
#### 4.1
Aufbau eines TCP-Headers nach RFC 793

0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |          Source Port          |       Destination Port        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                        Sequence Number                        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Acknowledgment Number                      |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Data |           |U|A|P|R|S|F|                               |
   | Offset| Reserved  |R|C|S|S|Y|I|            Window             |
   |       |           |G|K|H|T|N|N|                               |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |           Checksum            |         Urgent Pointer        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Options                    |    Padding    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                             data                              |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


#### 4.2 
Es gibt 3 Möglichkeiten eine Verbindung zu beenden:
1) normal Close Sequence - Verbindungspartener A sendet "FIN" an Partner B, dieser sendet Acknowledgement zurück, sendet selbts "FIN", wird von Partner A Acknowledged

2) simultan zu 1) - nur bekommt hier Partener A "FIN" zugesendet und muss darauf antworten usw.

3) Simultaneous Close Sequence -  beide Verbindungpartner senden gleichzeitig "FIN" und antworten sobald diese beim jeweils anderen eingetroffen sind mit einem Acknowledgement

#### 4.3
Acknoledgement Number/Sequence Number wird bei Überlauf wieder bei 0 angefangen zu inkrementieren. Dieser findet in diesem Szenario statt, da bis zu max. Anzahl von 2^32 nur noch 100 Bytes übrig sind, aber mehr Bytes (234 Bytes) gesendet werden sollen. 


### Aufgabe 5
Zweck bei Kommunikation:
es gibt Verwaltungsübertragungen zum Verbindungsauf- und abbau
und Datenübertragungen zum Übertragen von Daten

Falls Daten nicht erfolgreich übertragen,
wird kein Acknowledgement rückgesendet, nach bestimmter Zeit neue Datensendung 
bzw. bei Verbindungauafbau Neuversuche nach gewissem Timeout

### Aufgabe 6
Unterschiede UDP zu TCP
TCP viel zuverlässiger als UPD durch Acknowledgements nach Datensendung als Bestätigung, dass Daten angekommen sind, Paketnummerierung, Verbindungsaufbau...
Dadurch TCP viel aufwendiger als UDP, dieses aber deutlich unzuverlässiger, da nicht sichergestellt, dass Daten angekommen sind, und keine Verbindung aufgebaut wird

Vorteil UDP ggü TCP
- deutlich schneller/ weniger verbindungsbeanspruchend, da nur Datensendung

Nachteile UDP ggü TCP
- keine Paketnummerierung, keine Paketempfangsbestätigung
- Pakete können in falscher Reihenfolge ankommen
- Pakete können verlorengehen


### Aufgabe 7
#### 7.1
Hierbei handelt es sich um einen Client, da dieser durch s.connect() Verbindung zum Server herstellt, dann Daten sendet und nach Antwort die Verbindung durch s.close() schließt
Es wird wird TCP verwendet. Das ist erkennbar an dem Verbindungsaufbau.
#### 7.2
Client, da zunächst direkt Nachricht gesendet wird
UDP, da kein Verbindungasaufbau angefragt wird, Sockettyp = SOCK_DGRAM
#### 7.3
Server, da durch s.listen() auf Datensendung gewartet wird
TCP, da Sockettyp = SOCK_STREAM
#### 7.4
Server, da direkt Nachricht mittels s.recvfrom() empfanden wird
UDP, da Sockettyp = SOCK_DGRAM
