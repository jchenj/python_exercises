#! usr/bin/python3
# mcb.py - Saves & loads pieces of text to the clipboard

# Usage: mcb.py save <keyword> - Saves clipboard to keyword
#        mcb.py <keyword> - Loads keyword with copied text to shelf file
#        mcb.py delete <keyword> - Deletes keyword from shelf file
#        mcb.py list - Lists all keywords 
#        mcb.py delete - Deletes all keywords and text from shelf file

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print("Text added to mcb:", pyperclip.paste())
    elif sys.argv[1].lower() == 'delete':
        print("Deleting text from mcb: ", mcbShelf[sys.argv[2]])
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print("Keywords in mcb: ", str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print("Text ready to paste:", mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == "delete":
        mcbShelf.clear()
        print("All keywords deleted.")

    mcbShelf.close()

# Things I learned:
# Can't run .pyw files on Mac - use. py instead
# Make sure functions have all parentheses - lack of last ones in
    # if sys.argv[1].lower() == 'list': led to code not running
# Put in print statements to check code behavior
# Put in print statements as confirmations for user 
# Make sure to update usage so accurately reflects current code
# Make sure to put strings in quotations
    # e.g (if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
# dict.clear() deletes all keys and values from dictionary
    



