from termcolor import colored


class Banka:
    def __init__(self, ime, novac) -> None:
        self.ime = ime
        self.novac = novac

    def transfer(self, kome, koliko):
        if self.novac < koliko:
            return "Nemate dovoljno novca"
        self.novac -= koliko
        kome.novac += koliko
        return "Transfer uspesno izvrsen"


class Kupac:
    def __init__(self, ime, novac, banka) -> None:
        self.ime = ime
        self.novac = novac
        self.banka = banka

    def kupi(self, proizvod, pekara, kolicina):
        if pekara.proizvodi[proizvod].kolicina < kolicina:
            pekara.radnici[0].napravi(proizvod, pekara, kolicina)
        if pekara.proizvodi[proizvod].cena * kolicina > self.novac:
            top_up = input("Nemate dovoljno novca, da li zelite da doplatite? (da/ne)")
            if top_up == "da":
                kolicina_iz_banke = int(input("Koliko novca zelite da doplatite?"))
                if self.banka.novac < kolicina_iz_banke:
                    return "Nemate dovoljno novca na racunu"
                else:
                    self.novac += kolicina_iz_banke
            else:
                return "Nemate dovoljno novca"

        CENA = pekara.proizvodi[proizvod].cena * kolicina

        pekara.proizvodi[proizvod].kolicina -= kolicina
        pekara.zarada += CENA
        self.novac -= CENA
        return "Proizvod kupljen"


class Radnik:
    def __init__(self, ime) -> None:
        self.ime = ime

    def napravi(self, proizvod, pekara, kolicina):
        pekara.proizvodi[proizvod].kolicina += kolicina
        pekara.zarada -= pekara.proizvodi[proizvod].cena_da_se_napravi * kolicina
        return "Proizvod napravljen"


class Proizvod:
    def __init__(self, ime, cena, kolicina, cena_da_se_napravi) -> None:
        self.ime = ime
        self.cena = cena
        self.kolicina = kolicina
        self.cena_da_se_napravi = cena_da_se_napravi


class Pekara:
    def __init__(self, radnici, proizvodi):
        self.radnici = radnici
        self.proizvodi = proizvodi
        self.zarada = 0


banka = Banka("banka", 100000)

# radnici
r1 = Radnik("John")
r2 = Radnik("Bob")

# proizvodi
p1 = Proizvod("hleb", 80, 3, 50)
p2 = Proizvod("kifla", 70, 10, 40)
p3 = Proizvod("pizza", 300, 3, 200)

# kupci
pekara1 = Pekara([r1, r2], {"hleb": p1, "kifla": p2, "pizza": p3})
# pekara2 = Pekara([r1, r2], {"hleb": p1, "kifla": p2, "pizza": p3})

print(colored("Dobrodosli u pekaru", "magenta"))
print(colored(f"Radnici: {r1.ime}, {r2.ime}", "blue"))
print(colored(f"Proizvodi: {p1.ime}, {p2.ime}, {p3.ime}", "red"))

print("Kako se zovete?")
ime = input("Ime: ")
print("Koliko novca imate?")
novac = int(input("Novac: "))
kupac = Kupac(ime, novac, banka)

while kupac.novac > 0:
    print("Izaberite proizvod i kolicinu")
    proizvod = input("Proizvod: ")
    print(
        f"Kolicina: {pekara1.proizvodi[proizvod].kolicina} a cena je {pekara1.proizvodi[proizvod].cena}"
    )
    kolicina = int(input("Kolicina: "))
    rezultat_kupovine = kupac.kupi(proizvod, pekara1, kolicina)
    if rezultat_kupovine == "Nemate dovoljno novca":
        print(rezultat_kupovine)
        break

    print(colored(f"Zarada pekare: {pekara1.zarada}", "green"))
    print(colored(f"Novac kupca: {kupac.novac}", "green"))
