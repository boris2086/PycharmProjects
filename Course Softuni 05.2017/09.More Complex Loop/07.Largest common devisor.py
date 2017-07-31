a=int(input())
b=int(input())
while b!=0:
    oldb=b
    b = a%b
    a =oldb
print(a)
