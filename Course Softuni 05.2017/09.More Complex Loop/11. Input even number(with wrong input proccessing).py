n=0
while True:
    print('Enter even number: ',end='')
    try:
        n=int(input())
    except:
        print('Invalid number')
        continue
    if n %2==0:
        break
    print("The number is not even.")
print('Even number entered:',n)
