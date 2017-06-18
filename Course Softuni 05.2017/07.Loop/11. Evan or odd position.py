n = float(input())
even_sum=0
even_max=-1000000000.0
even_min=1000000000.0
odd_sum=0
odd_max=-1000000000.0
odd_min=1000000000.0


for i in range(1,n+1):
    curr = float(input())

    if (i%2==0):
        even_sum += curr
        even_max = max(even_max,curr)
        even_min = min(even_min,curr)
    else:
        odd_sum += curr
        odd_max = max(odd_max, curr)
        odd_min = min(odd_min, curr)
print('OddSum ={0:.2f}, OddMin={1:.2f}, OddMax={2:.2f}, EvenSum={3:.2f}, EvenMin={4:.2f}, EvenMax={5:.2f}'.format(even_sum,even_min,even_max,odd_sum,odd_min,odd_max))
