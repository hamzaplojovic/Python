print()

# Print je na engleskom ispisivanje, stampa
# Print je u Pythonu funkcija koja prima vrednost
# Print tu vrednost ispisuje
# U terminalu

# Terminal je prozorcic u vs code koji
# nam pomaze da vidimo rezultat naseg koda

# NOTE:
# print je u pythonu funkcija koja znaci ispisivanje
# koja ispisuje vrednost koju prima
#=====================================================
# Vrednost koju print prima mi nazivamo podatak
# podatak moze da bude 123, "hamza", True i False

# Da bismo organizovali podatke po slicnosti,
# koristimo razlicite tipove podataka

# Neki od njih su:
# integer - int - ceo broj (1,2, 3, 100, 100000, -1)
# float   - float - broj sa decimalom (1.3, 5.6, 9.8)
# string  - str - sve sto se nalazi izmedju dva navodnika
# boolean - bool - True False
# =====================================================
# Da ne bismo ponavljali vrednosti u kodu, jer to 
# krsi pravila programiranja, koristimo varijable

# Varijable su kontejneri za podatke koji nam sluze
# za cuvanje podataka za dalju upotrebu

# Varijable se pisu tako sto imamo dve strane koje
# su povezane znakom =. Desna strana je vrednost koju
# hocemo da cuvamo, leva je varijabla u koju je stavljamo
# Primer: x = 5
# ======================================================
# Operatori nam sluze za operacije nad podacima
# Postoje:
# Aritmeticki - (+, -, *, /, //, %, **)
# Za vrednost - (=, +=, -=, *=, /=, //=)
# Za uporedjivanje - (>, <, ==, !=, =>, <=)
# Logicki - (and, or, not)

# AND - True ako obe strane True
# OR - True ako bilo koja strana True
# NOT - NOT True (False), NOT False (True)
# =======================================================
# STRING JE "3i2desahiksgfckasgcbcsxz!"
# String moze da se pise u jednu ili vise linija
# "" jedna, """""" vise

# String je indeksiran
# Sto znaci da svaki karakter ima svoju poziciju
# Pozicija se naziva indeks, i obelezava se uglastim
# zagradama i indeksum izmedju njih - [0]

# indeks 0 je prvi element
# indeks 1 je drugi element
# indeks -1 je poslednji element

# NOTE:
# Indeksiranje je sistem organizovanja karaktera stringa,
# u kojem svaki karakter ima svoju poziciju, index.

ime = "Hamza"
print(ime[0])
print(ime[1])
print(ime[-1])

# Range na engleskom opseg
# Range se pise sa dva indeksa, start i end
# Range algoritam je:
# neki_indeks >= start and neki_index < end
# ime[1:5]  PRIMER: 1 >= 1 and 1 < 5

# Range je opseg u koji ukljucujemo sve karaktere
# stringa kojima je vrednost range algoritma True
# Range algoritam je algoritam koji uzima svaki indeks
# iz stringa i proverava je li indeks vece jednako start
# i manje od end
# PRIMER: Lista indeksa za "Hamza" je [0, 1, 2, 3, 4]
# PRIMER: range je 1:4
# PRIMER: 0 >= 1 and 0 < 4 False
#         1 >= 1 and 1 < 4 True
#         2 >= 1 and 2 < 4 True
#         3 >= 1 and 3 < 4 True
#         4 >= 1 and 4 < 4 False
#PRIMER: Prolaze: 1, 2, 3


