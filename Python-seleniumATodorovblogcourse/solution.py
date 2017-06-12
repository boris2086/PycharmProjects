import os

name = 'Ivan'

def sayHello(who):
    print ("Hello %s" % who)

class Person(object):
    pass

if __name__ == "__main__":
    sayHello(name)
    sayHello('Maria')
