myPets = ['Morzsi', 'Tomi', 'Taltos', 'Tinta']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name + '.')
else:
    print("Yes, I have a pet named " + name + ".")
    
