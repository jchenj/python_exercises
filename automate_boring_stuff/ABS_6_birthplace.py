print("Where were you born?")
place = input()
if place.lower() == 'texas' or 'san antonio':
    print("I was born in " + place[0].upper() + place[1:].lower()+ ", too.")
else:
    print("That's nice.")
