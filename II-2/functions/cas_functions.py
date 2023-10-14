# *args
# **kwargs
# rekurzija

dictionary = {
    "name": "ford",
    "model": "mustang",
    "year": 1964

}


def print_keys(dictionary):
    for x in dictionary.keys():
        print(x)

# print_keys(dictionary)


# def test(*args):
#     for x in args:
#         print(x)

# test(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

def test(**kwargs):
    for x in kwargs:
        print(x, "->", kwargs[x])


test(
    name="ford",
    model="mustang",
    year=1964,
    color="red",
    engine="v8",
    transmission="automatic",
    wheels="4",
    doors="2",
    passengers="4"
)

{
    "name": "ford",
    "model": "mustang",
    "year": 1964
}
