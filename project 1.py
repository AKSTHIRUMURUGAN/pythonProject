s=str(input("enter a sentence:"))
word=s.split()
l=len(word)
l11=[]
l22=[]


for i in word:
    s1=i[0]
    s2=i[-1]
    l11.append(s2)
    l22.append(s1)
l23=l22.pop(0)
for j in range(1,l):
    i1=l11[j-1]
    i2=l22[j-1]

if i1==i2:
    print("true")
else:
    print("false")











