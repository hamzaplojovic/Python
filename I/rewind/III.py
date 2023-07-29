# FUNKCIJE
# OPERATORI
# STRING METODE
# BOOLEAN TABELA
# IF ELIF ELSE
# ===============
# FOR LOOP
# LISTS
# TODO: WHILE LOOP

# moja_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 1, 1, 1]
# print(moja_lista[3])
# moja_lista[2] = 100000
# print(moja_lista[2])
# # [1, 2, 100000, 4, 5, 6, 7, 8, 9, 1, 1, 1, 1, 1, 1]

# moja_lista.append("hey")
# # [1, 2, 100000, 4, 5, 6, 7, 8, 9, 1, 1, 1, 1, 1, 1,"heys"]

# moja_lista.remove(4)
# # [1, 2, 100000, 5, 6, 7, 8, 9, 1, 1, 1, 1, 1, 1]

# moja_lista.clear()
# # []

# moja_lista = [1, 2, 3, 4]

# for x in moja_lista:
#     print(x)

kalendar = [
    ["10","11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"],
    ["10","11", "12", "13", "14", "15", "17", "18", "19", "20"],
    ["12", "13", "15", "16", "17", "18", "19", "20", "21"],
    ["10","11", "12", "13", "14", "15", "16", "17", "20", "21", "22"],
    ["10","11", "12",  "14", "15", "16", "17", "18"],
    ["10","11", "13", "14", "15",  "17", "18", "19", "20", "21", "22", "23"],
    ["10","11", "13", "14", "15",  "17", "18", "19", "20", "21", "22", "23"]
]

zeljeni_sat = input("Unesite zeljeno vreme: ")
zeljeni_dan = int(input("Unesite zeljeni dan: "))
rezultat = "Ne"

for dan in kalendar:
    for sat in dan:
        if kalendar[zeljeni_dan] == dan and sat == zeljeni_sat:
            rezultat = sat, "zeljeni sat", zeljeni_sat, "zeljeni dan", zeljeni_dan
            break


print(rezultat)