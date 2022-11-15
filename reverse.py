row = int(input("Enter the rows:"))
for i in range(row+1):
    for j in reversed(range(i,row+1)):
        print("*",end=" ")
    print()