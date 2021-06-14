myDictionary = {
    "work": "activity involving mental or physical effort done in order to achieve a purpose or result.",
    "tired": "in need of sleep or rest",  # never forget these comma
    "stress": "pressure or tension exerted on a material object",
    "atomic": "relating to an atom or atoms.",
    "temperature": [24, 28, 27, 32, 26, 33, 36],
    "travel": "go from one place to another",
    "another_dictionary": {"sad": "not happy"}
}
# we just made nested dictionary by putting "another_dictionry" in myDictionary
print(myDictionary['tired'])
print(myDictionary['another_dictionary']['sad'])
# lets change a value of a certain key
myDictionary['travel'] = "move"
print(myDictionary['travel'])
print(myDictionary)
empty_dictionary = {}
print(empty_dictionary)
