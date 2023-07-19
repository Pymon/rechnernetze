![net.png](/home/simon/studium/rechnernetze/altklausur/net.png)

## 3.

### N1 - 172.16.56.8

R1 172.16.56.9

H 172.16.56.10, 172.16.56.11

### N2 - 192.168.43.0

H 192.168.43.1

### N3 10.0.0.0

H 10.255.255.254, 10.0.0.1

b)

Routingtabelle für R1

| TARGET       | NETMASK         | GATEWAY    | INTERFACE |
| ------------ | --------------- | ---------- | --------- |
| 172.16.56.8  | 255.255.255.248 | 0.0.0.0    | eth2      |
| 192.168.43.0 | 255.255.255.0   | 0.0.0.0    | eth1      |
| 10.0.0.0     | 255.0.0.0       | 0.0.0.0    | eth0      |
| default      | 0.0.0.0         | 10.4.1.254 | eth0      |

c)

Entweder wurden weder N3 noch der default case in der Routingtabelle von R1 angelegt, oder bei beiden wurde ein falsches Interface angegeben oder N3 wurde nicht konfiguriert und R2 hat einen fehlerhaft konfigurierten default case.

4.

a)

| Name der Schicht    | Grundlegende Aufgabe                                  | Transmission Unit | Adresse            | Protokoll (Beispiel)     |
| ------------------- | ----------------------------------------------------- | ----------------- | ------------------ | ------------------------ |
| Transportschicht    | Anwendungsmultiplexing                                | Segment           | Port               | TCP, UDP, QUIC           |
| Vermittlungsschicht | Wegewahl, Subnetting                                  | Datagramm         | IP Adresse         | IPv4, IPv6, ICMP         |
| Anwendungsschicht   | Strukturierung der Kommunikation zwischen Anwendungen | Data              | (Well known Ports) | HTTP, DNS, POP3          |
| Netzzugriffschicht  | Erkennen von Übertragungsfehlern                      | Frame             | MAC                | CSMA/CD, Bluetooth, WLAN |

b)

MAC-Adressen sind lediglich für die physische Adressierung von Hardware gedacht. Erst durch IP-Adressen ist Kommunikation außerhalb des lokalen Netzes möglich, da es durch Subnetting einen hierarchischen Aufbau von Netzen und somit Routing ermöglicht.

c)

ARP (Address Resolution Protocoll)

5.

a)

```
d = 111
g = 1101
d' = 111000

111000 / 1101
1101
001100
  1101
  0001 -> CRC-Wert: 001
-> Übertragen wird: 111001
```

b)



6.

a) 
