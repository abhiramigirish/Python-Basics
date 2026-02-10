d={
    "a":1,
     "c":3,
    "b":2
   
}
for x,y in d.items():
    if y>=2:
        print(x,y)
print(sorted(d.items()))
x=sorted(d.items(), key=lambda item:item[1])
print(x)