n = float(input())
fromV = input()
toV = input()


usd = 1.79549
gpb = 2.53405
eur = 1.95583

tmp = n

if fromV == 'USD':
    tmp = n * usd
elif fromV == 'GBP':
    tmp = n * gpb
elif fromV == 'EUR':
    tmp = n * eur

if toV == 'USD':
    print(tmp / usd, 'USD')
elif toV == 'GBP':
    print(tmp / gpb, 'GBP')
elif toV == 'EUR':
    print(tmp / eur, 'EUR')

print('{0:.2f}'.format(tmp))
