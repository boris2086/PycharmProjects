type=input().lower()
r=int(input())
c=int(input())
prihod=-1

if type == 'premiere':
    prihod=r *c *12
elif type=='normal':
    prihod=r*c * 7.50
elif type=='discount':
    prihod=r*c*5
print('{0:.2f} leva'.format(prihod))

