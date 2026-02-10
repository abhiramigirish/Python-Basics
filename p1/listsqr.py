def sqr(n):
    l=[]
    for i in n:
        if i>0:
            l.append(i*i)
    return l

x=[1,-1,2,-2,3]
print (sqr(x))