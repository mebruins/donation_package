def login(database, username, password):
    if username in database:
        if database[username] == password:
            print('You are logged in as', username)
            return username
        else:
            print('Invalid password')
            return ''
    else:
        print('Invalid username')
        return ''


def register(database, username, password):
    if len(username) > 10 or len(password) < 5:
        print('Username too long or password too short. \nUsername must be 10 characters or less. \nPassword must be 5 chracters or more. ')
        return ''   
    elif username.lower() in database:
        print('Username already registered.')
        return ''
    else:
        print('Username registered.')
        return username

   
