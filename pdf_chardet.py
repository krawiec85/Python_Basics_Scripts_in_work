import PyPDF2
import os
import chardet

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
merger.write("Razem.pdf")
merger.close()
