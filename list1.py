books = ['Eric Matthes', 'sebastian raschka', 'Rubayet Alam']
print(books)
print(books[0].upper())
print(books[2].lower())
print(books[1].title())
'''before using any method like title, upper, 
 lower we must use index [0],[1], etc'''
# in python indexing starts from 0
print(books[-1])  # -1 starts from the end
print(books[-2])
# error, if we want 4 than in the list there must be 5 things/names/values
print(books[-0])
names = ["sayma", "ripa", "maria", "tania", "rubayet"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[-0])
print(names[-1])
print(names[-2])
print(names[-3])
# +0 or -0 both are same, they shows index [0]
text = "you are doing good"
message = f"{text} {names[4].upper()}"
print(message)
message = f"{text} {names[0].title()}"
print(message)
