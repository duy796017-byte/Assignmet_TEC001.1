def total(C):
    A = []
    for c in C:
        A.append(c)
    return A
def classify(D):
    B = []
    for d in D:
        if d % 2 == 0:
            B.append(d)
    return B
N = []
while True:
    M = input("Enter the numbers: ")
    if M == "":
        break
    try:
        M = int(M)
    except ValueError:
        print("Invalid value")
        continue
    N.append(M)
O = total(N)
P = classify(N)
print("All numbers:", O)
print("Even numbers:", P)
