class PrvaKlasa:
    class Sporet:
        def __init__(self) -> None:
            print("Sporet je pozvana")
            self.sta_je_unutra = "paprike"

    def __init__(self):
        novi_sporet = self.Sporet()
        self.sporet = novi_sporet
        self.ves_masina = "4 para carapa, 2 dukserice"
        print("Klasa je pozvana")


prvi_objekat = PrvaKlasa()
print(prvi_objekat.sporet.sta_je_unutra)
print(prvi_objekat.ves_masina)
