a=0
while a<5:
    username=input("enter username")
    password=input("Enter password")
    if username=="python" and password=="rules":
        print("Welcome")
        break
    else:
        print("uncorrected password or user name")
        a=a+1
    if a==5:
        print("access denied")
    else:
        None