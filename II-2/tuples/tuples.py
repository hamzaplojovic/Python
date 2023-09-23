# moja_lista = [1, 2, 3]
# # poredjana po indeksima
# # dozvoljava duplikate

# # TODO: mogu da se menjaju podaci unutar nje

# moja_lista[0] = 10
# print(moja_lista)

moj_tuple = (1, 2, 3)
moj_tuple = (1, 2, 3, True, 1.5, "dshiudsyf", [1, 2, 3], (1, 2, 3))
# poredjan po indeksima
# dozvoljava duplikate
# TODO: ne mogu da se menjaju podaci unutar njega
# print(len(moj_tuple))


# NAPISATI PROGRAM KOJI CE NACI KOJI ELEMENTI SE PONAVLJAJU.
# TUPLE: (1, 2, 3, 4, 5, 1, 1, 2, 3, 3, 10, 10)
moj_tuple = (1, 2, 3, 4, 5, 1, 1, 2, 3, 3, 10, 10)
duplicates = []

# ==================================================================
# PRVI NACIN
# ==================================================================
for x in moj_tuple:
    count = 0
    for item in moj_tuple:
        if item == x:
            count += 1
    if count > 1 and x not in duplicates:
        duplicates.append(x)

print(duplicates)
# ==================================================================
# PRVI NACIN
# ==================================================================

# ==================================================================
# DRUGI NACIN
# ==================================================================
# for x in moj_tuple:
#     item_count = list(moj_tuple).count(x)
#     if item_count > 1 and x not in duplicates:
#         duplicates.append(x)

# print(duplicates)