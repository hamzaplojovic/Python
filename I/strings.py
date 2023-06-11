# ime = """
#     Hamza
#     Plojovic
# """

# print(ime)

ime = "Python123"

# NOTE: [] ZAGRADE: ENGL Tastatura i desno pored P

# print(ime[0])
# print(ime[2])
# print(ime[-1])
# print(ime[-2])
# print(ime[-7:-1])

# print(ime[:6])
# od start do 6
# print(ime[6:])
# od 6 do end

# ime = "Hamza Plojovic"
# print(ime[3:6])

# ime = "Hamza.."
# print(len(ime))

# ime = "Hamza "
# prezime = "Plojovic"

# full_ime = ime + prezime
# print(full_ime)

# ime = "    Hamza     "
# ime_veliko = ime.upper()  # HAMZA
# ime_malo = ime.lower()  # hamza
# ime_bez_space = ime.strip()  # Hamza
# ime_a_u_e = ime.replace("a", "e")  # Hemze

# String Metode
# NOTE: .upper() => "ime" = "IME"
# NOTE: .lower() => "IME" = "ime"
# NOTE: .strip() => "   ime   " = "ime"
# NOTE: .replace("a", "e") => "IME" = "ime"


pozdrav = "HI, {}"

pozdrav_formatted = pozdrav.format("Ben")

print(pozdrav_formatted)
