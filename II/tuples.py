# moja_lista = [1, 2, 3]


# # for x in moja_lista:
# #     print(x)

# moja_lista[0] = 10

# print(moja_lista[0])

# ===================================================================================
# moj_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 3, 3)
# print(moj_tuple[2])
# print(moj_tuple.index(3))
# print(moj_tuple.count(3))

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
# print(8 in moj_tuple)

# ======================================================================
# moj_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1, 1)
# count
# print(moj_tuple.count(1))
# index
# print(moj_tuple.index(1))

# ======================================================================

# ZADATAK: COUNT metoda rucno
# Tuple, element u int(input("")), i da se vrati koliko se el pojavljuje u tuple

# element = int(input("Unesi element: "))
# moj_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 5, 65, 3, 2, 3, 2, 4, 545)

# # # Algoritam:
# count = 0
# moj_tuple = list(moj_tuple)
# for x in moj_tuple:
#     if x == element:
#         count += 1

# print(f"Broj: {element} se pojavljuje {count} puta")

# ======================================================================
# .INDEX METODA RUCNO
# Element u int(input) i da se vrati index na kojem je element
# element = int(input("Unesite neki broj: "))
# moj_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 3, 3, 3)

# for x in moj_tuple:
#     if x < element:
#         print("Element je na indeksu", moj_tuple.index(x))
#         break

# ========================================================


# NOTE: PRVI NACIN
# mytuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(mytuple[::-2])

# NOTE: DRUGI NACIN
# mytuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# nasa_lista = list(mytuple)
# nasa_lista.reverse()
# print(tuple(nasa_lista))

# ========================================================
# NOTE: DRUGI ZADATAK
# PYTHON PROGRAM KOJI PRIMA VREDNOST input("")
# PRETVARA STRING KOJI DOBIJE U TUPLE

# x = input("Unesi vrednoooooost: ")
# print(tuple(x))

# nasa_lista = []
# vrednost = input("Unesi vrednoooooost: ")
# for x in vrednost:
#     nasa_lista.append(x)
# print(tuple(nasa_lista))

# ========================================================
# NOTE: TRECI ZADATAK
# PYTHON PROGRAM KOJI IMA TUPLE POZITIVNIH BROJEVA
# I VRACA NAM SPOJENO

nas_tuple = (1, 2, 3, 4, 5, 6)
nas_string = ""

for x in nas_tuple:
    nas_string += str(x)

print(int(nas_string))
