color_list = ["red", "green", "blue", "yellow","white", "purple","magenta"]

print("Can you guess the colors I like?")

guess_color = input("enter your guess: ")

if guess_color in color_list:
    print("You are right!")
else: 
    print("Try again!")

    