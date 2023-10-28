# brojac = 0
# while brojac <= 10:
#     print("Trenutna vrednost", brojac)
#     brojac += 1


# WHILE PETLJA OZNACAVA BLOK KODA KOJI CE SE IZVRSAVATI SVE DOK JE USLOV KOJI JE ZADAN TACAN
# ONOG TRENUTKA KADA JE ZADATI USLOV NETACAN, TADA SE BLOK KODA U WHILE PETLJI NECE VISE IZVRSAVATI

# brojac = 0
# while brojac <= 10:
#     if brojac == 7:
#         print("Trenutna vrednost", brojac)
#         break
#     else:
#         print("Trenutna vrednost", brojac)
#         brojac += 1

# print("Petlja je zavrsena")

# BREAK JE PYTHON REC KOJA OZNACAVA DA SE PETLJA ZAVRSI
# U OVOM SLUCAJU, AKO DODJEMO DO VREDNOSTI BROJACA 7, MI ISPISEMO TRENUTNU
# VREDNOST I IZLAZIMO IZ PETLJE


brojac = 0
while brojac < 10:
    brojac += 1
    if brojac == 7:
        continue

    print(brojac)

print("Petlja je zavrsena")

# CONTINUE JE PYTHON REC KOJA OZNACAVA DA CE TRENUTNo PONAVLJANJE
# PETLJE DA SE PRESKOCI I DA CE DA SE NASTAVI SA SLEDECIM
