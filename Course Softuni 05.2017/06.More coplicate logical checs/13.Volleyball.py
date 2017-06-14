import math
year=input().lower()
p = int(input())
h=int(input())
game=0
weekends=48 - h
game=2*p/3
game +=weekends*3/4
game +=h
if year=='leap':
    game +=15*game/100
game=math.floor(game)
print(game)