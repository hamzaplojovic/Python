# NOTE: Funkcija je blok koda koji se izvrsava samo kada je pozvana
# U funkciju mogu da se proslede podaci, argumenti, parametri...
# Rezultat funkcije mogu biti podaci


# def print_name():
#     print("Hamza")


# print_name()


# def print_name(name):
#     print("Hello", name)


# name = input("Unesite ime: ")
# print_name("Clyde")


# def print_name(name, surname):
#     print("Hello", name, surname)


# print_name("Hamza", "Plojovic","33")


# def zbir(number1, number2):
#     return number1 + number2


# rezultat = zbir(1, 2)
# ====================================================
# Zadatak:
# Napisati funkciju koja dobija ARGUMENT neki string
# koji korisnik unese, i reversa string
# hamza => azmah


# def reverse_string(vrednost):
#     return vrednost[::-1]


# korisnik = input("Unesite neki string: ")
# rezultat = reverse_string(korisnik)
# print(rezultat)
# ============================================================================
# Zadatak:
# Napisati funkciju koja dobija ARGUMENT neki string
# koji korisnik unese, i proverava je li string palindrom


# def is_palindrom(vrednost):
#     if vrednost == vrednost[::-1]:
#         return True
#     else:
#         return False


# korisnik = input("Unesite vrednost: ")
# print(is_palindrom(korisnik))

actions = []


def main():
    def call_to_action(akcija):
        podatak = {"id": 0, "name": akcija}
        actions.append(podatak)

    akcija = input("Unesite akciju koju zelite da izvrsite: ")

    if akcija == "like":
        call_to_action("like")
    elif akcija == "share":
        call_to_action("share")
    elif akcija == "subscribe":
        call_to_action("subsribe")
    elif akcija == "save":
        call_to_action("save")

    print(actions)
    korisnik_input = input("Da li zelite da ponovite akciju: ")
    if korisnik_input == "da":
        main()
    else:
        print("Akcije zavrsene")


main()
