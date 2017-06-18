n=int(input())
if n >=1:
    Min=int(input())

for i in range(1,n):
    num=int(input())
    Min=min(Min,num)
print(Min)