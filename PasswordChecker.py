pass1=input('Enter Password: ')
pass2=input('Confirm Password: ')
if pass1 == pass2:
    print('Ok')
else:
    if pass1.casefold() == pass2.casefold():
        print('Please check for the cases and try again')
    else:
        print('Try them again')