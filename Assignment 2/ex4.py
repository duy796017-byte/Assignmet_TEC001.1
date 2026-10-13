Y=int(input("enter a year:"))
def check (A):
    if A%400==0 or (A%4==0 and A %100!=0):
        print("leap year")
    else:
        print("normal year")
check (Y)