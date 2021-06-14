first_list = [1, 8, 7, 2, 21, 15]
print(first_list)
first_list.sort()
print(first_list)
first_list.reverse()
print(first_list)
first_list.append(30)
print(first_list)
first_list.insert(3, 50)
print(first_list)
first_list.remove(7)
print(first_list)
first_list.pop(3)
print(first_list)
# it can be only used for string values
second_list = ['banana', 'apple', 'mango', 'lichi', 'berry', 'guava',
               'apple', 'watermelon', 'apple', 'grapes', 'lemon', 'apple']
second_list.pop(5)
print(second_list)
print(second_list.count('apple'))
second_list.remove('berry')
print(second_list)
fruits = second_list.copy()
print(fruits)
fruits.clear()
print(fruits)  # output--->[]
first_list[2] = 12
print(first_list)
