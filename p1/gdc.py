def gcd(a,b):
    while b!=0:
        a,b=b, a%b
    return a
n1=int(input("n1:"))
n2=int(input("n2:"))
print(gcd(n1,n2))