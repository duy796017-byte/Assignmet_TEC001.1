L=input("enter paragraph:")
A=L.split()
B=0
for i in A:
    i = i.strip(".,!?;:")
    if i.isdigit():
        B+=int(i)
print(B)