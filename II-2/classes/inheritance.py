# class Osoba:
#     def __init__(self, ime, prezime, zanimanje):
#         self.ime = ime
#         self.prezime = prezime
#         self.zanimanje = zanimanje

#     def ispisi_zanimanje(self):
#         print("Ja sam", self.ime, self.prezime, "i ja sam", self.zanimanje)


# class Programer(Osoba):
#     def __init__(self, ime, prezime):
#         super().__init__(ime, prezime, "programer")


# class Pekar(Osoba):
#     def __init__(self, ime, prezime):
#         super().__init__(ime, prezime, "pekar")


# novi_programer = Programer("Hamza", "Plojovic")
# novi_pekar = Pekar("John", "Smith")

# novi_programer.ispisi_zanimanje()
# novi_pekar.ispisi_zanimanje()


class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def print_car(self):
        print(self.name, self.model, self.year)


class BMW(Car):
    def __init__(self, model, year):
        super().__init__("BMW", model, year)


class Mercedes(Car):
    def __init__(self, model, year):
        super().__init__("Mercedes", model, year)


novi_bmw = BMW("X5", 2020)
novi_mercedes = Mercedes("C Class", 2021)

novi_bmw.print_car()
novi_mercedes.print_car()
