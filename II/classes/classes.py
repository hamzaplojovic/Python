# TODO: Klasa je plan po kojem pravimo objekat
# class MojaKlasa:
#     frizider = 5
#     televizor = 2
#     klima = 10

#     # Klasa salje self hteo ti to ili  ne
#     def ispisi_parametre(
#         self,
#     ):  # self je pokazivac koji pokazuje na sam objekat u kome se metoda nalazi.
#         print(self.televizor, self.klima, self.frizider)


# # TODO: objekat je proizvod koji nastaje kada se klasa pozove
# moj_objekat = MojaKlasa()
# # TODO: parametri objekta su identicni parametrima klase, i sastavni su deo OOP
# # TODO: OOP - Objektno Orijentisano Programiranje

# # print(moj_objekat.televizor)

# moj_objekat.ispisi_parametre()


# class MojaKlasa:
#     frizider = 5
#     televizor = 2
#     klima = 10

#     def ispisi_parametre(self):
#         print(self.televizor, self.klima, self.frizider)


# moj_objekat = MojaKlasa()


# moj_objekat.ispisi_parametre()


# __init__ funkcija je funkcija koja se automatski izvrsava kada od klase ( plana ) napravimo objekat ( kucu )
class Osoba:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


hamza = Osoba("Hamza")
kadir = Osoba("Kadir")
john = Osoba("John")
hamza.print_name()
kadir.print_name()
john.print_name()
