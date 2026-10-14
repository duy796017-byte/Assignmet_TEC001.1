s=None
l=None
while True:
    a=input("enter numbers:")
    if a=="":
        break
    a=float(a)
    if l is None or a>l:
        l=a
    elif s is None or a<s:
        s=a
print("smallest number", s)
print("largest number", l)