import PyPDF2

File = open("Hacking the Hacker.pdf", "rb")

pdfReader = PyPDF2.PdfFileReader(File)
print(pdfReader.numPages)
i=0
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())
print("Done!!!")
