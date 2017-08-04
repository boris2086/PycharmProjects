import math
n=int(input())

if n < 2:
    print('Not prime')
else:
    prime = True
    for i in range(2,int(math.sqrt(n))+1):
        if n % i==0:
            print('Not prime')
            prime=False
            break
    if prime:
        print('Prime')