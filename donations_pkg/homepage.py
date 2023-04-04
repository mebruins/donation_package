def show_homepage():
    print('          ==== DonateMe ====         ')
    print('-------------------------------------')
    print('| 1. Login      | 2. Register       |')
    print('-------------------------------------')
    print('| 3. Donate     | 4. Show Donations |')
    print('-------------------------------------')
    print('            5. Exit                  ')
    print('-------------------------------------')


def donate(username):
    donation_amt = float(input('Enter amount to donate: $'))
    if donation_amt <= 0:
        print('Not valid amount. Please enter amount greater than $0.')
    elif donation_amt > 0: 
        donation_string = username + ' donated $' + str(donation_amt)
        print(donation_string)
        print('Thank you,', username + '!')
        return donation_string




def show_donations(donations):
    print('\n--- All Donations ---')
    if len(donations) == 0:
        print('Currently no donations.')
    else:
        for donation in donations:
            print(donation)
