n = int(input("enter a number : "))
for i in range(n):
    for j in range(n-i):
        print(" ", end='')
    for k in range(2*i+1):
        print(k, end='')
    print()
    
