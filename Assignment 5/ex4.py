def cal(L):
    T=0
    for i in L:
        T+=i
    return T
A=[]
try:
    while True:
        C=int(input("enter numbers: (enter 0 to end)"))
        if C!=0:
            A.append(C)
        elif C==0:
            break
except ValueError:
    print("Value Error")
B=cal(A)
print(B)