#! /usr/bin/env python3
# bulletPointAdder - adds wikipedia bullets to the start of each line of text
# on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines & add stars
lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexes in the "lines" list
    lines[i] = '*' + lines[i]   # add star to each string in "lines" list

text = '\n'.join(lines)
    
pyperclip.copy(text)

