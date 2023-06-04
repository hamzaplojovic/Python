names = ["Adam", "John", "Mary", "Jane", "Bob"]
heights = [180, 170, 160, 165, 175]

my_dict = {}
sorted_names = []

for name, height in zip(names, heights):
    index = len(sorted_names)
    my_dict[index] = height
    sorted_names.append(name)

sorted_indices = sorted(my_dict.keys(), key=lambda x: my_dict[x], reverse=True)

print([sorted_names[index] for index in sorted_indices])
