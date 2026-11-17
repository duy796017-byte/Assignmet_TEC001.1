L=[]
while True:
    N=(input("Enter numbers:"))
    if N!= "":
        try:
            N=int(N)
            L.append(N)
        except ValueError:
            print("Error value")
    elif N=="":
        break
L.sort(reverse=True)
print(L[0:6])