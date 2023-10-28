class Osoba:
    def __init__(self, ime, prezime, zanimanje):
        self.ime = ime
        self.prezime = prezime
        self.zanimanje = zanimanje

    def ispisi_zanimanje(self):
        print("Ja sam", self.ime, self.prezime, "i ja sam", self.zanimanje)


novi_programer = Osoba("Hamza", "Plojovic", "programer")
novi_pekar = Osoba("John", "Smith", "pekar")
novi_policajac = Osoba("John", "Doe", "policajac")

novi_programer.ispisi_zanimanje()
novi_pekar.ispisi_zanimanje()
novi_policajac.ispisi_zanimanje()
