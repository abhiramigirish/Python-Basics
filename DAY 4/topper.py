d={}
n= int(input("enter number of students : "))
for i in range(n):
    key=input("enter name : ")
    value=int(input(f"enter {key}'s mark : "))
    d[key]= value
topper= max(d, key=d.get)
print("the topper is ", topper)