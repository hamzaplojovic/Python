# moja_lista = [1, 2, 3]

# # for x in moja_lista:
# #     print(x)

# moja_lista[0] = 10

# print(moja_lista[0])

# ===================================================================================
# moj_tuple = (1, 2, 3)
# moj_tuple_duplikati = (1, 2, 3, 3, 3, 3, 3, 3, 3, 3)
# moj_tuple_tipovi = (True, 1, 1.5, "dishdsudfhfsu", (1, 2, 3))

# moj_tuple[0] = 10
# print(moj_tuple[0])

# print(len(moj_tuple))
# print(moj_tuple_tipovi)

# moja_lista = [1, 2, 3]
# moj_tuple = tuple(moja_lista)

# print(moj_tuple)

# ======================================================================
# moj_tuple = (1, 2, 3, 4, 5, 6, 7, 8)

# print(moj_tuple[2:5])
# print(moj_tuple[:5])
# print(moj_tuple[2:])
# print(9 in moj_tuple)

# ======================================================================
# moj_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1, 1)
# count
# print(moj_tuple.count(1))
# index
# print(moj_tuple.index(5))

# ======================================================================

# ZADATAK: COUNT metoda rucno
# Tuple, element u input(""), i da se vrati koliko se el pojavljuje u tuple

# element = 2
# moj_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 5, 65, 3, 2, 3, 2, 4, 545)

# # Algoritam:
# count = 0
# moj_tuple = list(moj_tuple)
# for x in moj_tuple:
#     if x == element:
#         count += 1

# print(f"Broj: {element} se pojavljuje {count} puta")

# ======================================================================
# .INDEX METODA RUCNO
# Element u int(input) i da se vrati index na kojem je element
moj_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 3, 3, 3)
element = int(input("Unesite neki broj: "))

for x in moj_tuple:
    if x == element:
        print(f"Index elementa {element} je {moj_tuple.index(x)}")
        break
