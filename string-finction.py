print(len("rubayet"))
#string functions------->>>>

passage = "nuclear energy provide zero carbon electricity, most reliable and cheap one. This energy is better than renewable energy! If we talk about wind power or solar or hydro, nuclear takes lowest place and produces maximum energy. And obviously we should come out of oil/gas/coal powered energy sources and their applications"
#len is used to count all the string characters
print(len(passage))
#endswith is used to verify the last word or last character in a string/passage/word/line
print(passage.endswith("applications"))
print(passage.endswith("rubayet"))
print(passage.endswith("e"))
#lets find out how many e or any other characters/words are there in the passage
print(passage.count("e"))
print(passage.count("energy"))

#lets captialize energy in the passage

print(passage.capitalize())

#lets find any word from the given passage, we will find the word "carbon"

print(passage.find("carbon")) # 4 will come as answer
#here indexing starts from 0, so nuclear-->0, energy-->1,provides-->2,zero-->3, carbon-->4

#lets replace the word "provide" with "produce"

print(passage.replace("provide", "produce")) 

print("Nuclear is good.\n it \tis best for \\ all.")