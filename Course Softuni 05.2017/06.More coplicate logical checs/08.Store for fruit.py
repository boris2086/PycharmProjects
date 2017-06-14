fruit=input().lower()
day_of_week=input().lower()
quontity=float(input())
price=-1.0


if day_of_week=='saturday' or day_of_week=='sunday':
        if  fruit=='banana':
            price = quontity * 2.70
        elif fruit=='apple':
            price= quontity * 1.25
        elif fruit=='orange':
            price=quontity * 0.90
        elif fruit =='grapefruit':
            price=quontity * 1.60
        elif fruit == 'kiwi':
            price=quontity * 3.00
        elif fruit=='pineapple':
            price=quontity * 5.60
        elif fruit=='grapes':
         price=quontity * 4.20
elif day_of_week=='monday' or day_of_week=='tuesday' or day_of_week=='wednesday' or day_of_week=='friday' or day_of_week=='Thursday':
        if fruit=='banana':
            price = quontity * 2.50
        elif fruit=='apple':
            price= quontity *1.2
        elif fruit=='orange':
            price=quontity * 0.85
        elif fruit=='grapefruit':
            price=quontity * 1.45
        elif    fruit == 'kiwi':
            price=quontity * 2.70
        elif fruit=='pineapple':
            price=quontity * 5.50
        elif fruit=='grapes':
            price=quontity * 3.85

if price>=0:
    print("{0:.2f}".format(price))
else:
    print('error')




