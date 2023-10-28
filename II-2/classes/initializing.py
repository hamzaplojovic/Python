class PrvaKlasa:
    def __init__(self):
        self.ves_masina = "4 para carapa, 2 dukserice"
        print("Klasa je pozvana")

    def __sta_je_unutra(self):
        print(self.ves_masina)

    def contents_klase(self):
        self.__sta_je_unutra()


prvi_objekat = PrvaKlasa()
prvi_objekat.contents_klase()
