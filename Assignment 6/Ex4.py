A={}
T=input("enter text:")
S=T.split()
for word in S:
    if word in A:
        A[word]+=1
    else:
        A[word]=1
print(A)