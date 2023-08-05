# Inheritance je kada klasa koju pravimo nasledjuje sve
# property-je i methode neke druge klase
# Nova klasa na nasledjeno moze da dodaje nove property-je i methode
# dok cuva stare od klase od koje ih je nasledila


class Osoba:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_osoba(self):
        print(f"Osoba {self.name} ima {self.age} godina")


class Student(Osoba):
    def __init__(self, name, age):
        super().__init__(name, age)

    def print_student(self):
        print(f"Student {self.name} ima {self.age} godina i student je")


hamza = Osoba("Hamza", 15)
hamza_student = Student("Hamza", 15)


class Auto:
    def __init__(self):
        self.vrata = True
        self.hauba = True
        self.gepek = True
        self.retrovizor = True


class BMW(Auto):
    def __init__(self):
        super().__init__()
        # Auto.__init__()
        self.marka = "BMW"

    def print_auto(self):
        return self.vrata, self.hauba, self.gepek, self.retrovizor

    def print_marka(self):
        return self.marka


class Krs(BMW):
    def __init__(self):
        super().__init__()
        self.gepek = "Pun"
        self.vrata = "Razvaljena"
        self.hauba = "Nema je"
        self.retrovizor = "U gepek"


moj_bmw = BMW()
# print(moj_bmw.print_auto())
# print(moj_bmw.print_marka())

moj_krs = Krs()
# print(moj_krs.print_auto())

# INHERITANCE JE PRINCIP OBJEKTNO ORIJENTISANOG PROGRAMIRANJA
# TO JE KADA KLASA NASLEDJUJE DRUGU KLASU
# SUPER() JE POKAZIVAC NA KLASU KOJU NASLEDJUJEMO
# PARAMETRI I METODE SE MOGU MENJATI NAKON NASLEDJIVANJA

# ===============================================================================================================
# ===============================================================================================================
# ===============================================================================================================

# NAPISATI KLASU OSOBA KOJA U __INIT__ PRAVI 3 parametra: ime, adresa, godina rodjenja
# i njoj metodu koja izracuna kolika to osoba ima godina na osnovu ovih parametara


class Osoba:
    def __init__(self, ime, adresa, godina_rodjenja):
        self.ime = ime
        self.adresa = adresa
        self.godina_rodjenja = godina_rodjenja
        self.trenutna_godina = 2023

    def print_godine(self):
        return f"{self.ime} ima {self.trenutna_godina - self.godina_rodjenja} godina"


hamza = Osoba("Hamza", "Novi Pazar", 2008)
print(hamza.print_godine())
