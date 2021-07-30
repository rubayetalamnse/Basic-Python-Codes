
# You can access the docstring through the run time using the syntax: funcName.__doc__

#Example: 

def shout(word):
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + "!")

print (shout.__doc__)
shout("spam")

# Try to run it. :