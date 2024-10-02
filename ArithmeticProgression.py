n=int(input('Enter initial term:'))
m=int(input('Enter common Difference:'))
t=int(input('Enter Number of Terms:'))
for i in range(n,n+t*m,m):
    print(i)