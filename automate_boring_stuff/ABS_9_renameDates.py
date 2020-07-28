#! usr/bin/python3
# ABS_9_renameDates.py - renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

# Create a regex that can identify the text pattern of American-style dates.
# Call os.listdir() to find all the files in the working directory.
# Loop over each filename, using the regex to check whether it has a date.
# If it has a date, rename the file with shutil.move().

import shutil, os, re

# Create a regex that can matches file with the American date format.
datePattern = re.compile(r"""^(.*?)   # all text before the date
    ((0|1)?\d)-                       # one or two digits for the month
    ((0|1|2|3)?\d)-                   # one or two digits for the day
    ((19|20)\d\d)                     # four digits for the year
    (.*?)$                            # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory & match them against the regex
for amerFileName in os.listdir('.'):
    mo = datePattern.search(amerFileName)

    # Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename
    euroFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    
    # Get the full, absolute paths
    absWorkingDir = os.path.abspath('.')
    amerFileName = os.path.join(absWorkingDir, amerFileName)
    euroFileName = os.path.join(absWorkingDir, euroFileName)

    # Rename the files
    print('Renaming "%s" to "%s"...' % (amerFileName, euroFileName))
    shutil.move(amerFileName, euroFileName) # uncommented after testing




