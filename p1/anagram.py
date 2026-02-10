def anagram(a,b):
    if sorted(a)==sorted(b):
        return a,b
w1=str(input("enter the word1"))
w2=str(input("enter the word2"))
if anagram(w1,w2):
    print("ana")
else:
    print("not")