n=int(input())
Sum=0
Max=0
for i in range(n):
    current=int(input())
    Sum+=current
    Max = max(Max,current)
if Max == Sum-Max:
    print('Yes\nSum = {0}'.format(Max))
else:
    print('No\nDiff = {0} '.format(abs(Max-(Sum-Max))))
