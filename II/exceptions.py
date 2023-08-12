# Try, Except, Else, Finally

# TODO:==============================================================================
# try:
#     print(1 / 0)
# except:
#     print("Greska")
# TODO:==============================================================================


# NOTE:==============================================================================
# TRY Blok koda "POKUSAVA" da neki kod izvrsi, i ako postoji neka greska, onda
# se izvrsva kod u EXCEPT bloku
# NOTE:==============================================================================


# TODO:==============================================================================
# try:
#     print(1 / 0)

# except NameError:
#     print("Variable x is not defined")

# except ZeroDivisionError:
#     print("You are dividing by zero")

# except:
#     print("Something else went wrong")
# TODO:==============================================================================


# TODO:==============================================================================
# try:
#     print("Hello")
# except:
#     print("Greska")
# else:
#     print("Nema greske")
# TODO:==============================================================================


# TODO:==============================================================================
# try:
#     print("Hamza")
# except:
#     print("Greska")
# else:
#     print("Nema greske")
# finally:
#     print("Kraj")
# TODO:==============================================================================


# TODO:==============================================================================
# x = -1
# if x < 0:
#     raise Exception("Nema brojeva ispod zero")
# TODO:==============================================================================


# TODO:==============================================================================
# try:
#     print(1 / 0)
# except:
#     raise ZeroDivisionError("Nije dobro")
# TODO:==============================================================================


def divide(x, y):
    try:
        print(x / y)
    except ZeroDivisionError:
        print("Nije dozvoljeno deljenje sa 0")


x = int(input("Unesite broj: "))
y = int(input("Unesite broj: "))
divide(x, y)

# AKO je y ili x 0, da se ispisuje greska: "Nije dozvoljeno deljenje sa 0"
