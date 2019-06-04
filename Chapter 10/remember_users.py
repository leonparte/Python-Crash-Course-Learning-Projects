import json

filename = 'users.json'


def greeter(name):
    try:
        file = open(filename, 'r')
        usernames = ''
        for line in file.readlines():
            usernames += line
            if name in usernames:
                print('Welcome back, ' + name + '!')
            else:
                with open(filename, 'a') as f_obj:
                    json.dump(name, f_obj)
                    print('We will remember you when you come back, ' + name + '!')
    except FileNotFoundError:
        with open(filename, 'w') as f_obj:
            json.dump(name, f_obj)
            print('We will remember you when you come back, ' + name + '!')


while True:
    name = input('\nPlease enter your username to login or sigh up. '
                 'Otherwise you can enter "q" to quit:\n').title()
    if name == 'Q':
        print("Quit!")
        break
    else:
        greeter(name)