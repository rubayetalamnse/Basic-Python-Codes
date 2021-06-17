text = input("enter the text here\n")
if ("make a lot of money" in text):
    spam = True
    print("this text is spam: ")
elif ("click in this link" in text):
    spam = True
    print("this text is spam: ")
elif ("get iphone" in text):
    spam = True
    print("this text is spam: ")
elif ("watch this now" in text):
    spam = True
    print("this text is spam: ")
elif ("How I made 1 million" in text):
    spam = True
    print("this text is spam: ")
else:
    spam = False
    print("this text is not spam.")
#we need to find out why "this text is not spam keeps coming up"
    
