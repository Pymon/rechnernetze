## Lernblock 6: Anwendungschicht

### Aufgabe 1

#### Was ist ein FQDN?
FQDN = "Fully Qualified Domain Name"
vollständige und eindeutige Adresse einer Internetpräsenz
setzt sich aus Hostname und Domain zusammen
enthält alle Domain-Level (auch Toplevel-Domain)

#### Was ist ein Nameserver?
auch DNS-Server verwalten die Informationen, welche IP-Adresse zu welchem Domain-Namen gehört

#### Unterschied rekursiver und iterativer DNS-Abfrage
iterativ: bekommt auf Anfrage Antwort vom Server, bei welchem Server dieser als nächstes nachfragen soll, d.h. Client muss sich selber um weitere DNS-Frage kümmern

rekursiv: angefragter Server fragt anderen Server, der Server kennt, der Server kennt(usw...) der Antwort weiß nach dieser, gefragter Server fragt nächsten Server usw... gibt, sobald auf Anfrage Antwort bekommen diese an Client zurück - d.h. gefragter Server kümmert sich um DNS-Abfrage


### Aufgabe 2

#### 2.1
GET /informatik.html HTTP/1.1
Host: www.tu-chemnitz.de

#### 2.2
GET primär zur Abfrage von Nutzdaten/Anfordern eines best. Dokuments
- für Anwender in Adresszeile sichtbar
- URL-Parameter mit URL zsm gespeichert
- URL-Parameter unverschlüsselt gespeichert
- nur ASCII-Zeichen
- beschränkt auf max.-Länge der URL (2048 Zeichen)

POST primär zum Senden von Nutzdaten/Anhängen von Daten an existierendes Dokument
- für Anwender unsichtbar
- URL ohne Parameter gespeichert
- kann neben ASCII-Zeichen auch binäre Daten schicken
- URL-Parameter nicht automatisch gespeichert
- unbeschränkte Datenlänge

#### 2.3
200: alles Okay
404: Page Not Found 
500: Internal Server Error

#### 2.4
Bei modernen Browsern werden mehrere parallele Verbindungen genutzt, um die Bilder parallel zu laden, sobald das HTML-Dokument (inkl. CSS) geladen wurde.

(Screenshot von Wireshark)

#### 2.5
HTTP/1.1 Keep-Alive - wird vom Sender genutzt, um Verbindung zu Server aufrecht zu erhalten, man kann Timeout und max. Anzahl an Requests vor Verbindungsschließung festlegen

#### 2.6
Angabe zum Host zwingend für HTTP/1.1-Request nötig, da HTTP-Proxy-Server auf diese Angabe angewiesen ist/ diese erwartet
weil mehrere Websites mit unterschiedlichem Domainnamen sich eine IP-Adresse teilen und nur so unterschieden werden kann, welche angefragt wurde


### Aufgabe 3
Ein E-Mail-Programm...

#### prüft mittels POP3 die Mailbox auf neue E-Mails
auf Port 110 wird Verbindung aufgebaut, danach mit POP3-Kommandos mit USER und PASS authentifiziert, mit POP3-Kommando STAT wird zurückgegeben, wie viele Mails in der Mailbox liegen, mit RETR können diese dann abgerufen werden, mit QUIT kann Verbindung wieder getrennt werden

#### übermittelt eine neue E-Mail via SMTP an E-Mail-Anbieter
Verbindungsaufbau auf Port 25, mit Kommando HELO macht man sich bemerkbar (damit Server weiß, wer du bist), mit MAIL FROM: und RCPT TO: gibt man Absender und Empfänger der Mail an, danach mit Befehl DATA können die Mail-Daten geschickt werden (erst Header, dann Message) Ende der Nachricht markiert mit mit Zeile, die nur Punkt enthält
mit QUIT wird Verbindung abgebaut


### Aufgabe 4
siehe neue Datei :)