n=int(input())
oddSum=0
evenSum=0


for i in range(n):
    if i %2==0:
        evenSum +=int(input())
    else:
        oddSum += int(input())
if oddSum == evenSum:
    print('Yes\nSum = {0}'.format(oddSum))
else:
    print('No\nDiff = {0}'.format(abs(oddSum - evenSum)))
