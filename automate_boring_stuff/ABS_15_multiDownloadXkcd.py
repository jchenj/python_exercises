#! usr/bin/python3
# ABS_15_multiDownloadXkcd.py -> downloads all XKCD comics using multiple threads

import bs4
import os
import requests
import threading

url = 'http://www.xkcd.com'   # starting URL
print('Accessing %s...' % (url))
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd
print('Ready to download...')

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic + 1):
        # Download the page
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()
        
        soup = bs4.BeautifulSoup(res.text, features='html.parser')

        # Find the URL of the comic image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()

            # Save the images to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
                
# Create and start the Thread objects
downloadThreads = []        # a list of all the Thread objects
for i in range(0, 2300, 100):  # loop 23 times, create 23 threads. Need to have enough
                               # for all comics (2230 as of 11/20/2019)
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()
    
# Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')

'''Learning:
- Even if modifying existing program, need to understand differences to understand
what's needed & what now (i.e. way of going through pages is different in
multi-threaded version - didn't need "except requests.exceptions.MissingSchema;"
from earlier version
- For programs that need to run for a long time, can test by running on smaller
subset (i.e. running 3 threads to download 300 images instead of 23 to download 2300)
'''
