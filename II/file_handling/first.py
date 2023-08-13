# file = open("file.txt", "x")

# file.write("Hamza")

# OPEN() funkcija je ugradjena funkcija u pythonu koja se koristi za
# otvaranje fajla i vraca objekat fajla koji se moze koristiti za dalje
# manipulisanje fajlom.

# MODOVI:
# "r" - Čitanje - Podrazumevana vrednost. Otvara fajl za čitanje, greška ako fajl ne postoji
# "a" - Dodavanje - Otvara fajl za dodavanje, kreira fajl ako ne postoji
# "w" - Pisanje - Otvara fajl za pisanje, kreira fajl ako ne postoji
# "x" - Kreiranje - Kreira navedeni fajl, vraća grešku ako fajl već postoji
# ==================================================================================================================================================
# READING FILES:

f = open("file.txt")
print(f.read())

print(f.read(50))
print(f.readline())

f.close()
