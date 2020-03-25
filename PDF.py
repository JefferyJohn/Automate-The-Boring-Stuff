import PyPDF2, os

os.chdir(r'C:\Users\Jeffery John\PycharmProjects\Automate the Boring Stuff')
pdfFile = open(r'C:\Users\Jeffery John\PycharmProjects\Automate the Boring Stuff\UGAHacks 6 Sponsor Packet.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
reader.numPages

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())
