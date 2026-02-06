n= int(input("enter n : "))
a=0
b=1
c=a+b
for i in range(n):
    print(c, end=' ')
    a,b= b,c
  