n=int(input())
rows=n
fs=-1
ls=-1

if n%2==0:
    rows -=1
    fs=n//2
    ls=fs+1
else:
    fs=ls=n//2+1

for row in range(rows):
    for col in range(1,n+1):
        if col==fs or col==ls:
            print('*',end='')
        else:
            print('-',end='')
    if row >= rows//2:
        fs -= 1
        ls += 1
    else:
        ls-=1
        fs+=1
    print()