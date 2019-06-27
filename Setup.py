import sqlite3
import PyPDF2 

pdfFileObj = open('PDF\9791 PEREZ s1.pdf','rb') 

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pagenum = pdfReader.numPages

print('The Number Of Page is:',pagenum)

conn = sqlite3.connect('storetext.db')

c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS pdftotext (Page_number TEXT, Pdf_Text TEXT)')
conn.commit()

i=0
while (i < pagenum):
    print('Current Page Number :',i+1,end='\n\n')
    pageObj = pdfReader.getPage(i)
    finalextpage = pageObj.extractText()
    print(finalextpage,end='\n\n\n')
    c.execute("INSERT INTO pdftotext VALUES(?,?)",
              (i+1, finalextpage))
    conn.commit()
    i+=1
    

pdfFileObj.close()
input()
