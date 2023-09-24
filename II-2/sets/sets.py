# Setovi nisu poredjani po indeksima
# Setovi ne dozvoljavaju da se menjaju elementi
# Setovi ne dozvoljavaju duplikate

myset = {"apple", "banana", "cherry", "apple"}

# myset[0] = "hamza"

print(myset)


# Algoritam za izbacivanje duplikata iz liste
moja_lista = [1, 2, 3, 4, 5, 6, 1, 10, 1, 2, 1]
no_duplicates = []

for x in moja_lista:
    if x not in no_duplicates:
        no_duplicates.append(x)


print(no_duplicates)
print(list(set(moja_lista)))


# 1 zadatak:

prvi_set = {1, 4, 2, 10}
drugi_set = {6, 4, 11, 2}

# Ispisati dve linije:
# Prva linija da ispise brojeve koje drugi set ima a prvi nema
# Druga linija da ispise brojeve koje prvi set ima a drugi nema

razlika_prvog = drugi_set.difference(prvi_set)
razlika_drugog = prvi_set.difference(drugi_set)
print("Drugi ima a prvi nema", razlika_prvog)
print("Prvi ima a drugi nema", razlika_drugog)

# =============================================================================================================
myset.add(10)  # Dodavanje u set
myset.update(moja_lista)  # Dodavanje vise elemenata u set
myset.remove("cherry")  # Izbacivanje elementa
myset.discard("cherry")  # Izbacivanje elementa


# 2. zadatak

# Pitati korisnika da unese listu reci odvojene zarezom
# Napraviti listu u python od reci koje je korisnik uneo
# Izbrojati koliko puta se svaka rec ponavlja u listi reci
# Iz reci koje se ponavljaju jednom, ( nemaju duplikate ), naci slovo koje se u listi reci ponavlja najvise puta

# Na pr. Korisnik unese hamza, kadir, kerim, tahir, hamza, hana, hamza, hana, tahir
# [hamza, kadir, kerim, tahir, hamza, hana, hamza, hana, tahir]
# hamza - 3
# kadir - 1
# kerim - 1
# tahir - 2
# hana - 2

# kadir, kerim
# k - 2
# a - 12
# d - 1
# i - 4
# r - 4

# k - 2
# a - 12
# r - 4
# i - 4
# m - 4

# U listi koju je korisnik uneo, (hamza, kadir, kerim, tahir, hamza, hana, hamza, hana, tahir), od slova
# reci koje se ponavljaju jednom u listi, samo "d" se ponavlja samo jednom
