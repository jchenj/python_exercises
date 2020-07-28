import pprint

message = str.lower("STATELY, PLUMP BUCK MULLIGAN CAME FROM THE STAIRHEAD, bearing a bowl of lather on which a mirror and a razorlay crossed.")
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
