guest = ["seam","binoy","aryian","nabila","iffat","afsana"]
guest.sort()
print(guest)
#"sort" changes the order of the list in an alphabetical manner
guest.sort(reverse=True)
print(guest)
#using "reverse=True" we have reversed the whole sorted list
book = ["a crash course on python","python macine learning","fluent python", "python for data science","mathematics for machine learning"]
print("here is the original book list")
print(book)
print("\n Here is the sorted book list")
print(sorted(book))
#finding the length of a list
length_booklist= len(book)
print(length_booklist)