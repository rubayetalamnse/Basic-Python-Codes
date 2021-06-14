# adding elements to a list
# use "append" to add elements in a list
name = ["yeasa", "rubayet", "ariyan"]
name.append("seam")
print(name)
# append can have only one value at a time
name[2] = "mohammad"
print(name)
# here we changed the value of one member
# let's use insert
name.insert(0, "abdullah")
print(name)
# using insert we can fix in which position we want to add a value
# we can only add one value using insert.
del name[1]
print(name)
# using del we have to tell the index number
popped_name = name.pop()
print(popped_name)
# pop will just come out with only one value of the list
# this time "seam" was out of the list
# if we don't put index number in pop, it will cut out the last value
name.remove("rubayet")
print(name)
# we can use"remove" function to delete any value from the list
# to use remove we have to address the exact value within the parenthesis
younger = "mohammad"
name.remove(younger)
print(name)
print(f"{younger.upper()} is younger than Abdullah.")
