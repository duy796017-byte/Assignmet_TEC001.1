while True:
    try:
        N=(input("enter the number of month:(enter number)"))
        S=("spring", "summer", "autumn", "winter")
        M = int(N)
        if M==12 or M<=2:
            print(S[3])
        elif M<=5:
            print(S[0])
        elif M<=8:
            print(S[1])
        elif M<=11:
            print(S[2])
        elif M=="":
            break
    except ValueError:
            print("value error")
