num = list(map(int,input("Enter numbers separated by space: ").split()))
def fun(n):
    total=0
    for n in num:
        if n % 2==0:
            total +=n
    return total
print("sum of even numbers=", fun(num))



