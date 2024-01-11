x = int(input("Enter number: "))
temp = x
reverse = 0
while temp > 0:
    reminder = temp % 10
    reverse = (reverse * 10) + reminder
    temp = temp // 10
if x == reverse:
    print(x, "is paliandrome")
else:
    print(x, "is not paliandrome")

