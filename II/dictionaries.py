moj_recnik = {
    "name": "Hamza",
    "surname": "Plojovic",
    "age": "15",
    "job": "Full Stack Developer",
    "job": "Python Developer",
}

# NOTE: Recnik je tip podatka koji se sastoji iz kljuc-vrednost parova

# moje_ime = moj_recnik["name"]
# moj_posao = moj_recnik["job"]

# print(moje_ime)
# print(moj_posao)

# print(moj_recnik.keys())
# print(moj_recnik.values())

# moj_recnik["age"] = "16"
# print(moj_recnik)


# # NOTE: Dodavanje novog elementa u recnik
# moj_recnik["adresa"] = "Sarajevo"

# # NOTE: Dodavanje jednog dict-a na drugi
# moj_recnik.update({"adresa": "Sarajevo", "broj_telefona": "061-123-456"})

# # NOTE: Brisanje elementa iz recnika
# moj_recnik.pop("surname")
# print(moj_recnik)

# # NOTE: BRISANJE SVIH ELEMENTA IZ RECNIKA
# moj_recnik.clear()
# print(moj_recnik)


# ===========================================================================
# .keys()
# .values()
# .items() Listu tuple-ova (kljuc, vrijednost)

# for key, value in moj_recnik.items():
#     print(key + " ====> " + value)
# ===========================================================================


# Write a Python script to check whether a given key already exists in a dictionary.

# moj_dictionary = {
#     "name": "Hamza",
#     "surname": "Plojovic",
#     "age": "15",
# }

# varijabla kljuc koju korisnik unosi.
# ako postoji, vratiti vrednost pod tim kljucem
# ako ne, vratiti: "nepostojeci kljuc"

# kljuc = input("Unesite kljuc: ")
# if kljuc in moj_dictionary:
#     print(moj_dictionary[kljuc])
# else:
#     print("Nepostojeci kljuc")

# ===========================================================================
# Excersise 1
# Pomnoziti sve vrednosti u dictionary-ju:
# rezultat = 1
# moj_recnik = {
#     "broj_1": 10,
#     "broj_2": 23,
#     "broj_3": 48,
#     "broj_4": 126,
#     "broj_5": 800,
# }

# for x in moj_recnik:
#     rezultat *= moj_recnik[x]

# print(rezultat)

# ===========================================================================

# moj_recnik = {
#     "brojevi_1": [1, 3],
#     "brojevi_2": [4, 7, 8],
#     "brojevi_3": [10, 22, 38],
#     "brojevi_4": [167, 324, 9],
#     "brojevi_5": [1289, 4562, 2],
# }

# for x in moj_recnik:
#     moj_recnik[x] = sum(moj_recnik[x])

# print(moj_recnik)
# ===========================================================================

# moj_recnik = {
#     "Cierra Vega": 12,
#     "Alden Cantrell": 12,
#     "Kierra Gentry": 12,
#     "Pierre Cox": 12,
# }
# if len(set(moj_recnik.values())) == 1:
#     print(True)
# else:
#     print(False)
# Proveriti da li su sve vrednosti u recniku iste
# Program treba da vraca True ili False

# moj_dictionary = {" B M W": 100, " AU DI": 75, "MER C E D ES": 50}
# novi_dictionary = {}


# for k, v in moj_dictionary.items():
#     novi_dictionary[k.replace(" ", "")] = v

# print(novi_dictionary)
# ============================================================================================
moj_dictionary = {
    "BMW": 100,
    "AUDI": 75,
    "MERCEDES": 50,
    "BMW": 100,
}
duplicates = []
keys = []

# for x in moj_dictionary.keys():
#     keys.append(x)

# for x in keys:
#     if keys.count(x) > 1:
#         duplicates.append(x)
