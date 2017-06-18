price_vegetable=float(input())
price_fruit=float(input())
kg_vegetable=float(input())
kg_fruit=float(input())

sum_vegetable=price_vegetable * kg_vegetable
sum_fruit=price_fruit * kg_fruit
sum = sum_vegetable + sum_fruit
eu_sum = sum/1.94
print(eu_sum)