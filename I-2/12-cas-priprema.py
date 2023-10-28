# PRIPREMA ZA TEST

# 4 pitanja 2 zadatak
# 6 pitanja 1 zadatak

# PITANJA:
# 1. Sta je print() i cemu sluzi?
# 2. Nabroji tipove podataka koje smo radili
# 3. Sta je integer?
# 4. Sta je boolean?
# 5. Koji su to aritmeticki operatori?
# 6. Sta oznacava znak == ?
# 7. Sta je oznacava if, a sta else?
# 8. Sta je while petlja

# ZADACI:
# 1. Korisnik unosi svoje ime. Program ime prebacuje u sva velika slova i vraca izmenjeno ime
# 2. Napraviti FizzBuzz. Napraviti program koji za while petljom ide od 0 do 100, i za svaki od
#    brojeva izmedju 0 i 100 proverava:
#    Ako je broj deljiv sa 3, ispisuje Fizz
#    Ako je broj deljiv sa 5, ispisuje Buzz
#    Ako je broj deljiv sa 3 i 5, ispisuje FizzBuzz
#    Inace ispisuje broj
# =====================================================================================
# =====================================================================================
# =====================================================================================
# RAD:

# PITANJA
# 1. Print je funkcija u pythonu koja ispisuje ono sto joj je zadato u konzoli
# 2. Integer, Float, String, Boolean
# 3. Integer je ceo broj
# 4. Boolean je tip podatka cije vrednosti mogu biti True ili False
# 5. +, -, *, /, //, %, **
# 6. Znak == uporedjuje dve vrednosti sa desne i leve strane i kaze nam jesu li jednake
# 7. If oznacava blok koda koji ce se izvrsiti ako je uslov tacan, a else oznacava
#    blok koda koji ce se izvrsiti ako je uslov u if-u netacan
# 8. While petlja oznacava blok koda koji ce se ponavljati dok je uslov tacan


# ZADACI:
# 1.
ime = input("Unesi svoje ime: ")
ime_velika_slova = ime.upper()
print(ime_velika_slova)

# 2.
broj = 1
while broj <= 100:  # 33
    if broj % 3 == 0 and broj % 5 == 0:
        print("FizzBuzz")
    elif broj % 3 == 0:
        print("Fizz")
    elif broj % 5 == 0:
        print("Buzz")
    else:
        print(broj)
    broj += 1
