allGuests = {'JC': {'forks': 2, 'sardines': 1, 'chocolate bars': 3}, 'Fuki': {'bubbles': 2, 'forks': 1, 'chocolate bars': 1},'PM': {'sardines': 2, 'forks':2}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print('- Bubbles    ' + str(totalBrought(allGuests, 'bubbles')))
print('- Chocolate bars    ' + str(totalBrought(allGuests, 'chocolate bars')))
print('- Forks    ' + str(totalBrought(allGuests, 'forks')))
print('- Sardines    ' + str(totalBrought(allGuests, 'sardines')))



