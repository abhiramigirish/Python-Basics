n = str(input("enter the word : "))
d={}
for i in n:
    d[i]= d.get(i, 0)+1
print(d)