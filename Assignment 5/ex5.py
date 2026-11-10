def sor(S):
    A=[]
    for s in S:
        if s%2==0:
            A.append(s)
        else:
            continue
    return A
B=[]
try:
    while True:
        C=int(input("enter numbers: (enter 0 to end)"))
        if C!=0:
            B.append(C)
        else:
            break
except ValueError:
    print("Value Error")
D=sor(B)
print(D)