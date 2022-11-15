n = int(input("Enter the row: "))
for i in range(n):
    if i==n-1:
        print("+"*9)
    else:    
        print(" "*4 + "+")
    
for i in range(n-1):
    print(" "*4 + "+")