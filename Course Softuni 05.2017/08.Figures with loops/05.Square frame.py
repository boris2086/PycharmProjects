n=int(input())
print('+',end=' ')
for i in range(n-2):
    print('-',end=' ')
print('+')

for i in range(n-2):
    print('| ',end='')
    for j in range(n-2):
        print('- ',end='')
    print('|')
print('+',end=' ')
for i in range(n-2):
    print('-',end=' ')
print('+')