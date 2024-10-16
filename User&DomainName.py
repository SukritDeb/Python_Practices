a = input('Enter your email ID: ')
b = a.find('@')
print('User ID:', a[:b])
print('Domain:', a[b+1:])