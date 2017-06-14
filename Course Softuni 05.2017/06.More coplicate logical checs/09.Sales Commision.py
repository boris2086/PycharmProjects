town=input().lower()
s=float(input())
commision='error'

if town=='sofia':
    if 0<=s<=500:
        commision=s * 5/100
    elif 500<s<=1000:
        commision=s*7/100
    elif 1000<s<=10000:
        commision=s*8/100
    elif s>10000:
        commision=s * 12/100
elif town=='varna':
    if 0<=s<=500:
        commision=s * 4.5/100
    elif 500<s<=1000:
        commision=s*7.5/100
    elif 1000<s<=10000:
        commision=s*10/100
    elif s>10000:
        commision=s * 13/100
elif town=='plovdiv':
    if 0<=s<=500:
        commision=s * 5.5/100
    elif 500<s<=1000:
        commision=s * 8/100
    elif 1000<s<=10000:
        commision=s*12/100
    elif s>10000:
        commision=s * 14.5/100

    print("{0:.2f}".format(commision))

