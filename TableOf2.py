a = 2
x = int(input("Enter the number: "))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(a*j,end="")
        if(j==i):
            for k in reversed(range(1,i)):
                print(a*k,end="")
    print()
