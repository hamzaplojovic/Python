# moja_lista = [1, 2, 3, 4, 5, 5, 5, 5, 5, "Hamza", 4.3, True, [1, 2, 3]]

# Indexed
# print(moja_lista)
# print(moja_lista[-2])

# Kako menjamo vrednost elementa u listi?
# moja_lista[0] = 100
# print(moja_lista[0])


fake_list = [1, 2, 3]
# LIST METHODS
# .append(element) - dodaje element na kraj liste
# .insert(index, element) - dodaje element na odredjeni index
# .remove(element) - uklanja element iz liste
# .pop(index) - uklanja element sa odredjenog indexa

# fake_list.append("Python")
# fake_list.append(True)
# fake_list.append(3.14)
# fake_list.append([3, 4, 5])

# fake_list.insert(1, 100)

# fake_list.remove(2)
# fake_list.remove(3)

# fake_list.pop(1)

# print(fake_list)


# ZADACI:

# NAPISATI PROGRAM KOJI CE U DATOJ LISTI DA NADJE SVAKI ELEMENT
# DUZI OD N SLOVA

# KORISNIK UNOSI BROJ N
# LISTA RECI JE ["Python", "Java", "C++", "C#", "JavaScript", "PHP", "Ruby", "C", "Go", "Swift", "Kotlin"]

# reci = [
#     "Python",
#     "Java",
#     "C++",
#     "C#",
#     "JavaScript",
#     "PHP",
#     "Ruby",
#     "C",
#     "Go",
#     "Swift",
#     "Kotlin",
# ]
# n = int(input("Unesite broj n: "))
# reci_vece_od_n = []

# for x in reci:
#     if len(x) > n:
#         reci_vece_od_n.append(x)

# print(reci_vece_od_n)
# +=========================================================================
# NAPISATI PROGRAM KOJI ISPISUJE RAZLIKU ELEMENATA IZMEDJU DVE LISTE
# [2, 3, 5, 6]
# lista1 = [1, 2, 3, 4, 5, 6]
# lista2 = [1, 7, 10, 4, 100]

# razlika = []

# for x in lista1:
#     if x not in lista2:
#         razlika.append(x)

# print(razlika)

# ===========================================================================
# NAPISATI PYTHON PROGRAM KOJI CE SVAKOM ELEMENTU U LISTI
# DA PROMENI INDEKS ZA + 1

# [0, 1, 2, 3, 4, 5]
# [1, 0, 3, 2, 5, 4]
lista = [0, 1, 2, 3, 4, 5]
nova_lista = []
for x in range(0, len(lista), 2):
    sublista = [lista[x], lista[x] + 1][::-1]
    nova_lista.append(sublista[0])
    nova_lista.append(sublista[1])

print(nova_lista)
