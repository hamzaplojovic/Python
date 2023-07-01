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

moj_dictionary = {
    "name": "Hamza",
    "surname": "Plojovic",
    "age": "15",
}

# varijabla kljuc koju korisnik unosi.
# ako postoji, vratiti vrednost pod tim kljucem
# ako ne, vratiti: "nepostojeci kljuc"

kljuc = input("Unesite kljuc: ")
if kljuc in moj_dictionary:
    print(moj_dictionary[kljuc])
else:
    print("Nepostojeci kljuc")
