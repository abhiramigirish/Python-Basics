n=int(input("enter the no to check armstrong"))
temp=n
total=0
p=len(str(temp))
while temp>0:
    d=temp%10
    total=total+d**p
    temp=temp//10
    
if total==n:
    print("armstrong")
else:
    print("not a")
