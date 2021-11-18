!pip install pyttsx3
!pip install PyPDF2


import pyttsx3
import PyPDF2

# creating the speaker
sp = pyttsx3.init()

# opening the book and reading using module
book = open('Google-Nvidia.pdf','rb')
PDFReader = PyPDF2.PdfFileReader(book)

# total pages
pages = PDFReader.numPages

for n in range(11, pages):
    # getting the page and extracting text from it
    page =PDFReader.getPage(n)
    text = page.extractText()

    # calling the speaker to say text
    sp.say(text)
    # it gives the appropriate timing offset
    sp.runAndWait()
