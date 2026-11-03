import re
A= input("Enter university course codes:")
if len(A) ==6:
    B=re.findall(r"[A-Z]{3}[0-9]{3}",A)
    if B:
        print("True")
    else:
        print("False")
else:
    print("False")