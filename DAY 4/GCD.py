a = int(input("enter the first number : "))
d_a=[]
for i in range(1, a+1):
    if a % i==0:
        d_a.append(i)
b = int(input("enter the second number : "))
d_b=[]
for j in range(1, b+1):
    if b % j==0:
        d_b.append(j)
cd=[]
for i in d_a:
    for j in d_b:
        if i==j:
            cd.append(i)
print("CD=", cd)
GCD=max(cd)
print("gcd=", GCD)


