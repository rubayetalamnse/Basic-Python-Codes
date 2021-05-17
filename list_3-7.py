guest = ["seam","binoy","aryian","nabila","iffat","afsana"]
cancel1= guest.pop(0)
print(guest)
print(f" I am sorry {cancel1.upper()}, I can't invite you in the dinner.")
cancel2= guest.pop(1)
print(guest)
print(f" I am sorry {cancel2.upper()}, I can't invite you in the dinner.")
cancel3= guest.pop(2)
print(guest)
print(f" I am sorry {cancel3.upper()}, I can't invite you in the dinner.")
cancel4= guest.pop(2)
print(guest)
print(f" I am sorry {cancel4.upper()}, I can't invite you in the dinner.")
print(guest)
print(f"{guest[0]}, you are still invited in  my dinner")
print(guest)
print(f"{guest[1]}, you are still invited in  my dinner")
del guest[0]
print(guest)
del guest[1]
print(guest)

