n=int(input("Enter a number in the range [1...100] "))
while not (1<=n<=100):
    print("Invalid number!")
    n=int(input("Enter a number in the range [1...100] "))
print("The nuber is:", n)
