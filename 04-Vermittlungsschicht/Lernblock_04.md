## Lernblock 4: Vermittlungsschicht 

### Aufgabe 1
#### Warum wird eine neue Adresse benötigt, wenn in der Sicherungsschicht bereits die global eindeutigen MAC-Adressen eingeführt wurden?
MAC-Adressen nur in lokalem Netz verfügbar, zum Verbinden zwischen einzelnen Netzen wird IP-Adresse benötigt, um zu wissen, in welches Netz die Nachricht geschickt werden soll: Routing

#### Wie kann ein Gerät die MAC-Adresse eines Empfängers im gleichen Subnetz bestimmen, wenn nur die IP-Adresse bekannt ist?
durch senden von Broadcast mit IP-Adresse -  derjenige mit dieser IP-Adresse antwortet dann darauf mit seiner MAC-Adresse

### Aufgabe 2
IPv4-Adresse 192.168.1.188
Netzwerk mit Netzmaske 255.255.255.224 oder /27

    192.168.1.188 → binär:
  11000000.10101000.00000001.10111100
    255.255.255.224 → binär
& 11111111.11111111.11111111.11100000
  11000000.10101000.00000001.10100000
  → dezimal: 192.168.1.160 → Netzwerk


Die letzten 5 Bit der Adresse sind frei vergebbar, allerdings nicht 00000 - das ist die Adresse zur Selbstadressierung und auch nicht 11111 - das ist die Broadcastedresse


### Aufgabe 3
IPv4-Netzwerk 134.109.42.0
Netzmaske 255.255.254.0

#### 3.1
134.109.42.102 → ist drin
#### 3.2
134.109.41.153 → ist nicht drin
#### 3.3
134.109.43.234 → ist drin


### Aufgabe 4

#### Routingtabelle Router 1
Ziel              Gateway          Netzmaske        Flags  Interface
192.168.100.128   *                255.255.255.192  U      eth1 
10.25.6.0         192.168.100.130  255.255.255.0    UG     eth1 
10.1.0.0          192.168.100.130  255.255.0.0      UG     eth1 
192.168.43.0      192.168.100.130  255.255.255.0    UG     eth1 
192.168.42.0      192.168.100.130  255.255.255.0    UG     eth1 
default           213.187.69.48    0.0.0.0          UG     eth0 

#### Routingtabelle Router 2
Ziel                Gateway          Netzmaske        Flags  Interface
192.168.100.128     *                255.255.255.192  U      eth0 
10.25.6.0           *                255.255.255.0    U      eth1 
10.1.0.0            *                255.255.0.0      U      eth2 
192.168.43          10.25.6.45       255.255.255.0    UG     eth1 
192.168.42          10.25.6.45       255.255.255.0    UG     eth1 
default             192.168.100.129  0.0.0.0          UG     eth0

#### Routingtabelle Router 3
Ziel                Gateway          Netzmaske        Flags  Interface
192.168.42          *                255.255.255.0    U      eth1
192.168.43          *                255.255.255.0    U      eth2
10.25.6.0           *                255.255.255.0    U      eth0 
default             10.25.6.22       0.0.0.0          UG     eth0



### Aufgabe 5
Unterschiede zwischen IPv6 und IPv4 in  Bezug auf Subnetze
-  

### Aufgabe 6

### Aufgabe 7

### Aufgabe 8

#### Aufgabe 9
#### 9.1 von A zu G
A → E → G mit 6

#### 9.2 von B zu D
B → A → C → D mit 7


### Aufgabe 10
Die Nachricht wird an den Absender mit einer entsprechenden Fehlermeldung zurückgeschickt