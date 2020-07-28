#! /usr/bin/env python3            # Allows the script to run from the command line on OSX.
# numberedListMaker - This script takes paragraph(s) and makes into a numbered list

import pyperclip            #imports a Python module for copy and paste clipboard functions.
text = pyperclip.paste()    # sets text as whatever is currently on the clipboard

# Separate lines & add numbers
lines = text.split('.')     # Splits text into a list of sentences. Because the text is split on all periods,
                            # the code won't work properly if there are periods other than end of sentence. Future work? :)
                            
for i in range(len(lines)):          # Loops through all sentences, adding numbers to the beginning of each.
    if len(lines[i]) < 2:            # This avoids adding a new line at the end of the list, with just the line number & no text
        break
    else:
        lines[i] = str(i+1) + '. ' + lines[i].strip() + '.' 

text = '\n'.join(lines)     # Joins list sentences back into one string. 

pyperclip.copy(text)        # Replaces text on the clipboard with the newly formatted version. 
    
