diameter1=int(input("enter the diameter of pizza 1 (cm):"))
diameter2=int(input("enter the diameter of pizza 2 (cm):"))
price1=int(input("enter the price of pizza 1 (USD)"))
price2=int(input("enter the price of pizza 2(USD)"))
area1=(((diameter1/2)**2)*3.14)
area2=(((diameter2/2)**2)*3.14)
value1=(area1/price1)
value2=(area2/price2)
if value1>value2:
    print("the pizza 1 is more value than pizza 2")
elif value2>value1:
    print("the pizza 2 is more value than pizza 1")
else:
    print("both pizza have the same value")
