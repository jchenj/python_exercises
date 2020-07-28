#! /usr/bin/python3
# ABS_13_combinePDFs.py - Combine all PDFs in current working directory into a
# single PDF. 

import PyPDF2
import os

# Get all PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

# Sort PDFs in alphabetical ordder
pdfFiles.sort(key=str.lower)

# Create object to hold combined PDF pages
pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all PDF files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Loop through all pages (except first) and add them
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save resulting PDF to a file
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
print('Done')
