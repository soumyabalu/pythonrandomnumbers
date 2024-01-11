a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
c = int(input("Enter num3: "))
if a > b and a > c:
    print(a, "is the maximum number")
elif b > a and b > c:
    print(b, "is the maximum number")
else:
    print(c, "is the maximum number")
