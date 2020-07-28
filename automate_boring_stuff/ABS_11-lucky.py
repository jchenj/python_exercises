#! usr/bin/python3
# lucky.py -> Opens several Google search results

"""Couldn't get the code to work - the linkElems list kept ending up empty"""

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, features='html.parser')

# Open a browser tab for each result
linkElems = soup.select('.r a')  # Finds all <a> elements within an element
                                # with the r CSS class

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
