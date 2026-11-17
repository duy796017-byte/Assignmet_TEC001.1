N=set()
while True:
    name = input("Enter a name: ")
    if name == "":
        break
    if name in N:
        print("Existing name")
    else:
        print("New name")
        N.add(name)
print("Names:")
for name in N:
    print(name)
