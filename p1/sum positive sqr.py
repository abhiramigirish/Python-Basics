
def sqr(n):
    a=[]
    for i in n:
        if i>0:
            a.append(i*i)
    return a
l=[1,2,3,4,5,6,-1,-2]

print(sqr(l))