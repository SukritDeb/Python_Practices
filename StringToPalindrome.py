a = input("Enter the string: ")
r = a[::-1]
if(a == r):
    print("Already a Palindrome")
else:
    print(a + r)