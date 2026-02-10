def anagram(a,b):
    a=a.lower()
    b=b.lower()
    return sorted(a)==sorted(b)

w1= str(input("enter the first word : "))
w2= str(input("entyer the second word : "))

if anagram(w1,w2):
    print("words are anagram")
else:
    print("words are not anagram")