import pyttsx3

friend = pyttsx3.init()
speech= input("Say Something: ")
#friend.say("nuclear energy provide zero carbon electricity, most reliable and cheap one. This energy is better than renewable energy! If we talk about wind power or solar or hydro, nuclear takes lowest place and produces maximum energy. And obviously we should come out of oil/gas/coal powered energy sources and their applications")
friend.say(speech)
friend.runAndWait()