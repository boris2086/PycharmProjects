product=input().lower()
town=input().lower()
quantity=float(input())


if town == "sofia":
    if product == "coffee":
        print("{0:.2f}".format(quantity*0.50))
    elif product == 'water':
        print("{0:.2f}".format(quantity * 0.80))
    elif product== 'beer':
        print("{0:.2f}".format(quantity * 1.20))
    elif product == 'sweets':
        print("{0:.2f}".format(quantity * 1.45))
    elif product == 'peanuts':
        print("{0:.2f}".format(quantity * 1.60))
elif town == "plovdiv":
    if product == "coffee":
        print("{0:.2f}".format(quantity * 0.40))
    elif product == 'water':
        print("{0:.2f}".format(quantity * 0.70))
    elif product== 'beer':
        print("{0:.2f}".format(quantity * 1.15))
    elif product == 'sweets':
        print("{0:.2f}".format(quantity * 1.30))
    elif product == 'peanuts':
        print("{0:.2f}".format(quantity * 1.50))
elif town == "varna":
    if product == "coffee":
        print("{0:.2f}".format(quantity * 0.45))
    elif product == 'water':
        print("{0:.2f}".format(quantity * 0.7))
    elif product== 'beer':
        print("{0:.2f}".format(quantity * 1.10))
    elif product == 'sweets':
        print("{0:.2f}".format(quantity * 1.35))
    elif product == 'peanuts':
        print("{0:.2f}".format(quantity * 1.55))