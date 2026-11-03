def hex(C):
    if len(C)!=7:
        return False
    for i in range(1):
        if C[i] !="#":
            return False
    for i in range(1,7):
        if C[i] not in "0123456789abcdefABCDEF":
            return False
    return True
H=input("enter hex-color code:")
F=hex(H)
if F==True:
    print("Valid code")
else:
    print("invalid code")