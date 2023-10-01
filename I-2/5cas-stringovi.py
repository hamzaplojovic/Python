ime = "hamza12345678910"

#print(ime[2])

# Prvi problem: Ne znamo koji je poslednji, pretposlednji...
# zbog menjanja duzine stringa
# Resenje: Negativni indexi
# print(ime[-1])

# Drugi problem: Ako hocemo da ispisemo deo stringa duzine x
# Moramo da x puta pisemo string[index] dok ne dodjemo do zeljene
# duzine dela stringa
# Primer: hamza1234567 = amza12
# ime[1]+ime[2]+ime[3].....
# Resenje: Range (opseg) stringova koji ispisuje deo stringa od 
# pocetni_index:kranji_index - ime[2:6]
# print(ime[2:7])

# print("affan" in ime)
# print("affan" not in ime)



