import random
a=0
a=random.randint(1,10)
while True:
    b=int(input("guess the number (enter 1-10)"))
    if b==a:
        print("correct")
        break
    elif b>a:
        print("too high")
        b=0
    elif b<a:
        print("too low")
        b=0