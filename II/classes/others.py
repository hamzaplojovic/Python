# ENCAPSULATION
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         # __ime_atributa = privatan atribut
#         # moze da se koristi samo u toj klasi
#         self.__age = age

#     def get_age(self):
#         return self.__age


# hamza = Person("Hamza", 15)
# hamza_age = hamza.get_age()
# print(hamza.name, hamza_age)

# Enkapsulacija je proces skrivanja atributa tako da samo članovi te
# klase, čak ni podklasa te klase, nemaju pristup, osim metoda koje se
# nalaze u toj klasi
# ==================================================================
# Abstraction
# preskocili jer se koristi modul abc - Abstract Base Class
# =================================================================
# Polymorphism


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, self.age)


class Kinez(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def pricaj(self):
        print("zhōngwén")


class Britanac(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def pricaj(self):
        print("boota of watah")


kinez = Kinez("Bruce Lee", 90)
britanac = Britanac("Rowan Atkinson", 2)

for osoba in {kinez, britanac}:
    osoba.pricaj()
    osoba.print_info()
    osoba.pricaj()
