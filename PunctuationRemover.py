a = '''!@#$%^&*()_-+={}[]|\:;<,>.?/~`'''
b = ''
s = input('Enter a String: ')
for x in s:
    if x not in a:
        b += x
print(b)