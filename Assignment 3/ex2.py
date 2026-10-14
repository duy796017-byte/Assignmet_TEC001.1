a=0
while True:
    try:
        a = float(input("enter numbers(inches):"))
    except ValueError:
        print("invalid value")
    if a >= 0:
        print(a * 2.54,"centimetres")
    else:
        break
