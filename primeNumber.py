x = int(input("Enter number: "))
flag = False
if x > 1:
    for i in range(2, x):
        if x % i == 0:
            flag = True
            break
if flag:
    print(x, "is not a prime number")
else:
    print(x, " is a prime number")
