a = input('Enter the string: ')
l = ''
u = ''
for x in a:
    if x.islower():
        l+=x
    else:
        u+=x
s = l + u
print(s)