myDictionary = {
    "work": "activity involving mental or physical effort done in order to achieve a purpose or result.",
    "tired": "in need of sleep or rest", #never forget these comma
    "stress": "pressure or tension exerted on a material object",
    "atomic": "relating to an atom or atoms.",
    "travel":"go from one place to another",
    "write": "mark on something, paper, surface, etc",
    "funny": "causing laughter or amusement",
    "sad":"feeling sorrow"
}
print("you can see the meaning of only these words: ",myDictionary.keys())
a = input("enter the word whose meaning you want to know: ")
#print("the meaning of your word is: ",myDictionary[a])
print("the meaning of your word is: ",myDictionary.get(a))
#using get function will not cause any error even your desired word is not in the dictionary, it will simply show "none"