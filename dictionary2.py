person = {
    "Name":"Rubayet",
    "Age": 21,
    "HasAndroidPhone": True

}
print("{} is aged {}, and owns an {}.".format(
    person["Name"], 
    person["Age"], 
    "Android phone" if person["HasAndroidPhone"] else "iPhone"
))
