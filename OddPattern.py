x = int(input("Enter the number: "))
for i in range(x+1):
    for j in range(i+1):
        print((2*j)+1,end="")
        if(j==i):
            for k in reversed(range(i)):
                print((2*k)+1,end="")
    print()
