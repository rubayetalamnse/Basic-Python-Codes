#name = input("enter your name: ")
#print("Good Morning, " + name)

letter = '''Dear <|name|>
greetings from ABC company. I am happy to tell you that
\tYou are Selected
your joining date: <|Date|>'''
name= input("enter your name: ")
date= input("enter your joining date: ")
letter = letter.replace("<|name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)