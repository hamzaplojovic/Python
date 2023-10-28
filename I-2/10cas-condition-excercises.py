# x = 12

# if x == 12:
#     pass
# else:
#     print("X nije 10")


# ZADATAK: Korisnik unese rec, a program
# ispisuje rec u obrnutom redosledu
# PRIMER: hamza - azmah


# rec = input("Unesite rec: ")

# obrnuta_rec = rec[::-1]

# print(obrnuta_rec)


# ZADATAK: NAPISATI PROGRAM GDE KORISINIK UNOSI
# DVA BROJA, I PROGRAM IH SABIRA. AKO JE ZBIR
# IZMEDJU 15 i 20, PROGRAM VRACA BROJ 20
# U SUPROTNOM, SAMO ISPISATI ZBIR
# 7       7
# 9       6
# 20      13

prvi_broj = int(input("unesite prvi broj: "))
drugi_broj = int(input("unesite drugi broj: "))

zbir = prvi_broj + drugi_broj

if zbir >= 15 and zbir <= 20:
    print(20)
else:
    print(zbir)
