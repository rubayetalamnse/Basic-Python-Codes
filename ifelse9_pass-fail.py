bangla = float(input("enter the obtained mark for Bangla out of 100: "))
english = float(input("enter the obtained mark for english out of 100: "))
math = float(input("enter the obtained mark for math out of 100: "))
total_marks = 300
obtained_marks = bangla+english+math
percentage = ((obtained_marks)/total_marks)*100
#print(total_marks,percentage)
if (percentage>40 and bangla>33 and english>33 and math>33):
    print("you have passed!")
else:
    print("you have failed!")