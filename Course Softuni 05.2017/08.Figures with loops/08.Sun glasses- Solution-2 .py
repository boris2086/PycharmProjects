n=int(input())

print('*'*2*n,end='')
print(' '*n,end='')
print('*'*2*n)
for i in range(n-2):
    print('*',end='')
    print('/'*(n+1),end='')
    print('|',end='')
    print('*',end='')
    print('   *', end='')
    print('/' * (n + 1), end='')
    print('*')
print('*'*2*n,end='')
print(' '*n,end='')
print('*'*2*n)

