
#%%
#use pypdf library to merge multiple pdf files
#folder mai 2-3 pdf dalni padegi fir hum niche wale code se 
#merge kar payege.



from PyPDF2 import PdfWriter
import os

merger=PdfWriter()
files=[file for file in os.listdir() if file.endswith(".pdf")]

merger.write("merged-pdf.pdf")
merger.close()



