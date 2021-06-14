fruit_tuple = ("apple", "banana", "cherry")
updated_fruit_tuple = list(fruit_tuple)
updated_fruit_tuple[1] = "kiwi"
fruit_tuple = tuple(updated_fruit_tuple)
print(fruit_tuple)
