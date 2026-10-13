cabin=0
cabin=input("enter cabin class (A, B, C or LUX):")
def Class (C):
    if C == "A":
        print("above the car deck, equipped with a window")
    elif C == "B":
        print("windowless cabin above the car deck")
    elif C == "C":
        print("windowless cabin below the car deck")
    elif C == "LUX":
        print("upper-deck cabin with a balcony")
    else:
        print ("invalid cabin class")
Class (cabin)