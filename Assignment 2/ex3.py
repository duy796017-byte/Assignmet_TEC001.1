S=input("enter your biological sex(male/female)")
H=int(input("enter your hemoglobin value (g/l)"))
def check (A, B):
    if A=="female":
        if B <= 155:
            print("normal")
        elif B < 117:
            print ("low")
        else:
            print ("high")

    if A=="male":
        if B <= 167:
            print("normal")
        elif B < 134:
            print("low")
        else:
            print("high")
check (S, H)