P=input("enter a phrase:")
def Split (s):
    R=""
    A=s.split()
    for a in A:
        R+=a[0]
    print(R)
Split(P)