length=0
def check(L):
    if L >= 42:
        print("accept")
    else:
        print("your zander is less than", 42-L,"centimeters the size limit.","Please return it to the sea")
while length==0:
    try:
        length=float(input("Enter zander length (centimeters)"))
    except ValueError:
        print("invalid value")
check(length)