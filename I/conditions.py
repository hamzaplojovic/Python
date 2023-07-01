# a = 10
# if a > 5: # Preskace se ako je False
#     print("A je vece od 5") # Ispisace se ako je True
# print(100+200)

# NOTE: if u pythonu oznacava uslov
#       sastoji se iz reci if koja oznaca uslov
#       iz boolean operacije koja vraca True ili False
#       iz koda koji ce da se izvrsi ako je uslov True
#       ako je uslov false, nastavljamo izvan if grane

# a = 10
# if a > 5:
#     rezultat = "A je vece od 5"
#     print(rezultat)

# print(1+1)

# NOTE: ZADATAK
# KORISTITI int(input("Unesi prvi broj: ")) i
# int(input("Unesi drugi broj: ")) i pomnoziti ih
# i sa if proveriti je li proizvod veci od 100
# ako je veci od 100, ispisi proizvod je veci od 100

# ======================================================

# DRUGI CAS: DEEP DIVE


# moje_ime = ""

# if moje_ime == "Hamza":
#     print("Moje ime je Hamza")
# else:
#     print("Ime nije Hamza")

# Else u pythonu oznacava sve ostale slucajeve nakon if.
# To znaci da se izvrsava ako if nije True

# ======================================================

# moj_broj = 5
# if moj_broj > 5:
#     print("Moj broj je veci od 5")
# elif moj_broj == 5:
#     print("Moj broj je 5")
# elif moj_broj == 6:
#     print("Moj broj je 6")
# elif moj_broj == 7:
#     print("Moj broj je 7")
# else:
#     print("Error")

# NOTE: Elif se koristi u slucajevima kada imamo mnogo if uslova,
#       i da ne bismo svaki od if uslova proveravali, koristimo elif.

# Ako imamo 100 elif uslova, i jedan je tacan, 99 ostalih se ne proveravaju
# Ako imamo 100  if  uslova, i jedan je tacan, 99 ostalih se takodje proveravaju

# =======================================================================================

# unos varijabla
# proveravamo:
# ako je unos deljiv sa 3 - ispisemo Fizz
# ako je unos deljiv sa 5 - ispisemo Buzz
# ako je unos deljiv sa 3 i sa 5 - ispisemo FizzBuzz

# unos = int(input("Unesite broj: "))

# if unos % 3 == 0 and unos % 5 == 0:
#     print("FizzBuzz")
# elif unos % 3 == 0:
#     print("Fizz")
# elif unos % 5 == 0:
#     print("Buzz")
# else:
#     print(unos)

# =======================================================================================

# unos varijabla koja je string - unos = input("Unesite unos: ")
# proveravate ako unos moze da se PRETVORI U INTEGER
# ako moze, ispisati string je integer
# ako ne, ispisati error

unos = input("Unesite string: ")

if unos.isnumeric() == True:
    print("String je broj", int(unos))
else:
    print("error")
