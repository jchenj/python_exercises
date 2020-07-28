birthdays = {'Ivan': 'Feb 27', 'Fuki': 'April 5', 'Vijay': 'Sep 21'}

while True:
    print('Enter a name: (or just press Enter to quit).')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday info for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
              
