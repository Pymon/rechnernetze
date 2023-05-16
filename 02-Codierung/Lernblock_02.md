## Lernblock 2: Codierung

### Aufgabe 1

#### Was ist ein Code?
Codierung - eineindeutige Abbildung der Wortmenge A+ über einem
Alphabet A (Quellencode/ Information) auf die Wortmenge B+ über
einem Alphabet B
Code - Menge aller Codewörter, d.h. das Bild c(A+) → B+

#### Was ist ein Codewort?
Codewörter können aus beliebigen Wörtern, Sätzen, Zahlen oder Symbolen bestehen und müssen von den beteiligten Parteien vorher vereinbart werden, um sicherzustellen, dass sie den gleichen Code verwenden. Sie dienen dazu, klare Kommunikation in Situationen zu ermöglichen, in denen eine offene oder direkte Sprache nicht angemessen oder sicher ist.

(Als Codewort bezeichnet man die Verbindung mehrerer Code-Elemente. Die vereinbarte Anzahl von Code-Elementen kann beliebig groß sein. Ein m-stelliges Codewort besteht demnach aus m Code-Elementen.

Je nach Anzahl der diskreten Stufen oder Zustände des Code-Elements kann ein m-stelliges Codewort (n expm) Kombinationen bilden. Codewörter können aus einer Zeichen- und Symbolsequenz bestehen und müssen die spezifischen Regeln des Codes einhalten. Codewörter werden u.a. in der Kommunikation, in Fehlererkennungs- und Fehlerkorrekturcodes verwendet. Eines der bekanntesten Codewörter ist das aus dem internationalen Telegrafenalphabet bekannte SOS.

Ein Codewort kann auch ein verschlüsseltes Wort sein, mit dem sensitive Daten übertragen werden.)

#### Welche Eigenschaften haben die verschiedenen Arten von Binärcodes?
Binärcode: Codes die aus Codealphabet {1,0} bestehen

Blockcode: Codes in denen alle Codewörter gleiche Länge haben

Linearer Code: Code in dem Summe zweier Codewörter ebenfalls Codewort ist

Systematischer Code: Codes, in denen Codewörter mit Länge n aus m Informationsbits und n-m Prüfbits bestehen 

Zyklischer Code: durch bitweises Rotieren eines Codeworts entsteht ein weiteres gültiges Codewort

#### Was bedeutet Hamming-Abstand?
Anzahl der Stellen, an denen sich die Codeworte u und v eines Codes c unterscheiden

Bsp.: u = 111
      v = 000
      Hemmingabstand: 3

#### Was bedeutet Gewicht?
Anzahl der 1en in einem Codewort


### Aufgabe 2
     110100 
XOR  010110
-----------
     100010


### Aufgabe 3

#### 3.1
  0000000000
+ 0000000000
------------
  0000000000

  0000011111
+ 0000000000
------------
  0000011111

  1111100000
+ 0000000000
------------
  1111100000

  1111100000
+ 0000011111
------------
  1111111111 


#### 3.2
(um d Fehler zu Erkennen, muss Hemmingabstand min. d+1 sein)
Mit einem Hemmingabstand von 5 sind 4 Fehler erkennbar

#### 3.3
(um d Fehler zu korrigieren, muss Hemmingabstand min, 2*d+1 sein)
Mit einem Hemmingabstand von 5 sind 2 Fehler korrigierbar 


### Aufgabe 4

#### Das Null-Element ist stets ein gültiges Codewort, da...
...ein beliebiges gültiges Codewort A unseres linearen Codes bei Addition mit dem Nullelement stets das gültige Codewort A bleibt.

Bsp:
  1111100000
+ 0000000000
------------
  1111100000

#### Der Minimale Hammingabstand ist gleich dem minimalen Gewicht aller Codeworte, die ungleich Null sind
Hemmingabstand = Anzahl an 1en, der nach XOR-Operation zweier Codewörter übrig bleibt

[...to be completed...]


### Aufgabe 5

#### 5.1
d = 000 -> c = 000 000
d = 100 -> c = 100 101
d = 110 -> c = 110 011
d = 111 -> c = 111 000

#### 5.2
c = 001011 -> d = 001

#### 5.3
Beim Decodieren wird das Wort aus dem Code wiederhergestellt und beim Prüfen wird geprüft, ob es richtig ist.

#### 5.4
n = Länge des codierten Wortes
k = Länge der Information

Prüfmatrix:
p = 110 | 100
    011 | 010
    101 | 001

#### 5.5
011101 - ja
010100 - nein


