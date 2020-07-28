#! python3
# ABS_13_readDocx.py - Returns single string value of text in .docx file

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append('   ' + para.text)
    return '\n\n'.join(fullText)
