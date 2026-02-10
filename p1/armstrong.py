n=int(input("number;"))
temp=n
sum=0
l=len(str(n))
for i in range(l):
    digit=n%10
    sum+= digit**l
    n=n//10
if temp==sum:
    print("armstrong")
else:
    print("not")
