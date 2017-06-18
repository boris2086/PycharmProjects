n=int(input())
if n >=1:
    Max=int(input())

for i in range(1,n):
    num=int(input())
    Max=max(Max,num)
print(Max)