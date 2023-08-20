# Pekara:
# - radnici
# - proizvodi
# - metoda da se doda novi radnik
# - metoda da se doda novi proizvod
# - metoda da se doda novi kupac

# Kupac:
# - ime
# - novac
# - metoda da kupi neki proizvod u nekoj kolicini

# Radnik:
# - ime
# - metoda da proda neki proizvod u nekoj kolicini

# Proizvod:
# - ime
# - cena
# - kolicina

# instanciram pekaru, da dodam 2 radnika, 4 kupca, i po tri od svakog proizvoda
# i da kupac moze da kupi proizvod po zelji


class Kupac:
    def __init__(self, ime, novac) -> None:
        self.ime = ime
        self.novac = novac

    def kupi(self, proizvod, pekara):
        CENA = pekara.proizvodi[proizvod].cena

        pekara.proizvodi[proizvod].kolicina -= 1
        pekara.zarada += CENA
        self.novac -= CENA
        return "Proizvod kupljen"


class Radnik:
    def __init__(self, ime) -> None:
        self.ime = ime

    def napravi(self, proizvod, pekara):
        pekara.proizvodi[proizvod].kolicina += 1
        return "Proizvod napravljen"


class Proizvod:
    def __init__(self, ime, cena, kolicina) -> None:
        self.ime = ime
        self.cena = cena
        self.kolicina = kolicina


class Pekara:
    def __init__(self, radnici, proizvodi):
        self.radnici = radnici
        self.proizvodi = proizvodi
        self.zarada = 0


# radnici
r1 = Radnik("John")
r2 = Radnik("Bob")

# proizvodi
p1 = Proizvod("hleb", 5, 3)
p2 = Proizvod("kifla", 10, 10)
p3 = Proizvod("pizza", 20, 3)

# kupci
k1 = Kupac("Richard", 100)

pekara = Pekara([r1, r2], {"hleb": p1, "kifla": p2, "pizza": p3})
print("Kifli:", pekara.proizvodi["kifla"].kolicina)

print("Novac pre kupovina", k1.novac)
print(k1.kupi("kifla", pekara))
print("Novac nakon kupovina", k1.novac)
print("Zarada nakon kupovina", pekara.zarada)


print(r1.napravi("kifla", pekara))
print(r1.napravi("kifla", pekara))

print("Kifli:", pekara.proizvodi["kifla"].kolicina)
