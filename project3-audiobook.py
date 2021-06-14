import pyttsx3
import PyPDF2
book = open('ml-tut.pdf','rb')
book_reader = PyPDF2.PdfFileReader(book)
pages= book_reader.numPages
print(pages)
for num in range(10,pages):
    page=book_reader.getPage(num)
    text= page.extractText()
    my_friend = pyttsx3.init()
    my_friend.say(text)
    my_friend.runAndWait()