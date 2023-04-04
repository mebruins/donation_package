# I could only get bonus tasks 1 and 2 to work.
# 3 and 4 stumped me and due date was looming...
# Guess I'm not Pensky material...

from donations_pkg import homepage
from donations_pkg import user

database = {'admin': 'password123'}

donations = []
authorized_user = ''

while True:
    homepage.show_homepage()

    if authorized_user == '':
        print('You must be logged in to donate.')

    else:
        print('Logged in as:', authorized_user)

    option = input('Choose an option: ')

    if option == '1':
        username = input('Enter username: ')
        password = input('Enter password: ')
        authorized_user = user.login(database, username, password)

    elif option == '2':
        username = input('Enter username: ')
        password = input('Enter password: ')
        authorized_user = user.register(database, username.lower(), password)
        if authorized_user != '':
            database[username.lower()] = password

    elif option == '3':
        if authorized_user == '':
            print('You are not logged in.')
        else:
            donation_string = homepage.donate(authorized_user)
            donations.append(donation_string)

    elif option == '4':
        homepage.show_donations(donations)

    elif option == '5':
        print('Goodbye')
        break

    else:
        print('Choose a valid option.')
