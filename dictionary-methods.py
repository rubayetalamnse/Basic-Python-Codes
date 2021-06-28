myDictionary = {
    "work": "activity involving mental or physical effort done in order to achieve a purpose or result.",
    "tired": "in need of sleep or rest",  # never forget these comma
    "stress": "pressure or tension exerted on a material object",
    "atomic": "relating to an atom or atoms.",
    "temperature": [24, 28, 27, 32, 26, 33, 36],
    "travel": "go from one place to another",
    1: 2,
    "another_dictionary": {"sad": "not happy"}
}
# prints the keys of a dictionary----->
print(myDictionary.keys())
# find out the type of these keys---->
print(type(myDictionary.keys()))  # <class 'dict_keys'>
# print the keys in a list form
print(list(myDictionary.keys()))
# print the values in a list form
print(list(myDictionary.values()))
# now we will update the dictionary by adding new key and value
update_dictionary = {
    "write": "mark on something, paper, surface, etc",
    "funny": "causing laughter or amusement",
    "sad": "feeling sorrow"
}
myDictionary.update(update_dictionary)
print(myDictionary)
# easy way to update-------->
myDictionary.update({"exciting": "causing great enthusiasm and eagerness."})
print(myDictionary)
# lets find the value of a certain key------->
finder1 = myDictionary.get("stress")
print(finder1)

# without using get function we can directly use:
print(myDictionary['funny'])
# if a key is not present in the dictionary and we want to get that value we will see "none" but in the other way like "print(myDictionary['funny1'])" will show error.

# now we will remove a vlue and key from the dictionary
myDictionary.pop('write')
print(myDictionary)
# the popitem() method removes the last inserted item----->
myDictionary.popitem()
print(myDictionary)
# we inserted exciting at last, and its removed by popitem()
del myDictionary
print(myDictionary)
# we have deleted our previous dictionary using "del"
Dictionary_returns = {
    "work": "activity involving mental or physical effort done in order to achieve a purpose or result.",
    "tired": "in need of sleep or rest",  # never forget these comma
    "stress": "pressure or tension exerted on a material object",
    "atomic": "relating to an atom or atoms.",
    "temperature": [24, 28, 27, 32, 26, 33, 36],
    "travel": "go from one place to another",
    "another_dictionary": {"sad": "not happy"}
}
new_dictionary = Dictionary_returns.copy()
Dictionary_returns.clear()
print(Dictionary_returns)  # the output is ---> {}
# now we will print new_dictionary which is the copied version of Dictionary returns-->
print(new_dictionary)
d = {'x': 1, 'y': 2, 'z': 3} 
for key in d:
    print(key, 'corresponds to', d[key])