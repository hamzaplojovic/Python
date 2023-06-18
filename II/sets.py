# NOTE: Python Sets
# moj_set = {"apple", "banana", "cherry"}
# print(moj_set)

# NOTE: NO DUPLICATES
# moj_set = {"apple", "banana", "cherry", "apple"}
# print(moj_set)

# NOTE: DATA TYPES
# moj_set = {"nekistring", True, 0, 0.2, (0, 1, 2)}
# print(moj_set)

# ==================================================

# SET METHODS

# add
# remove
# clear
# discard
# pop
# update
# union
# difference and intersection

moj_set = {"apple", "banana", "cherry", "mango"}
moj_drugi_set = {"papaya", "grapes", "orange", "watermelon"}
moj_treci_set = {"bmw", "audi", "mercedes"}
moj_cetvrti_set = {"fiat", "audi", "bmw"}


# moj_set.add("ananas")   # Added ananas in set
# moj_set.remove("kiwi")  # Tried to remove, but error
# moj_set.discard("kiwi") # Tried to remove, but went past it
# moj_set.clear()         # void function, ne prima vrednost,  brise sve vrednosti
# moj_set.pop()           # Removes first element after initialization

# moj_set.update(moj_drugi_set)  # Added a set on the set the method is called on
# moj_set.union(moj_drugi_set)  # returns the value

razlika = moj_treci_set.difference(moj_cetvrti_set)
presek = moj_treci_set.intersection(moj_cetvrti_set)

# print(moj_set)
print(razlika)
print(presek)
