prvi_broj = int(input("Unesite prvi broj: "))
drugi_broj = int(input("Unesite drugi broj: "))

print("1) + je sabiranje")
print("2) - je oduzimanje")
print("3) * je mnozenje")
print("4) / je deljenje")

operacija = input("Unesite operaciju: ")

if operacija == "+":
    print("Rezultat je", prvi_broj+drugi_broj)
if operacija == "-":
    print("Rezultat je", prvi_broj-drugi_broj)
if operacija == "*":
    print("Rezultat je", prvi_broj*drugi_broj)
if operacija == "/":
    print("Rezultat je", prvi_broj/drugi_broj)
else:
    print("Nevazeca operacija")