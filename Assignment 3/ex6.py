def extract(x):
    G=list(x)
    N=len(G)
    M=N//2
    if x=="":
        print("None string")
    else:
        if N%2==0:
            print("the middle character are:", G[M-1],"and", G[M])
        else:
            print("the middle character is:", G[M])
S=input("enter a string:")
extract(S)