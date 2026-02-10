def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0

    for d in digits:
        total += d**power
    return total

# Input from user
num = int(input("Enter a number: "))

# Check and print result
if is_armstrong(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")

num1 = input('enter the number : ')
sum = 0
i = 0

while i < len(num1):
    a = num1[i]
    sum += int(a)**len(num1)
    i += 1

if sum == int(num1):
    print("Armstrong")
else:
    print("not Armstrong")

