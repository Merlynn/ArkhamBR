import PyPDF2
import os

DIR="D:\\Users\\PMMG\\Desktop\\drive-download-20240305T132653Z-001\\Guia de Campanha\\EN\\"

directory = os.fsencode(DIR)

merge = PyPDF2.PdfMerger()

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".pdf"):
        file = f"{DIR}{filename}"
        print( file )
        merge.append(file)
    else:
        continue

merge.write("All_Campaing_EN.pdf")