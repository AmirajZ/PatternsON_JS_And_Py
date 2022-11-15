# for i in range(5):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(1):
#         print("*",end="")    
#     print()
    
# for i in range(5):
#     for j in range(i,4):
#         print(" ",end="")
#     for j in range(1):
#         print("*",end="")    
#     print()

for i in range(5):
    print(" "*i+"*",end=" ")
    if i!=4:
        print((" ")*(10-2*i-3)+"*",end=" ")
    print()

for i in reversed(range(5)):
    print(" "*i+"*",end=" ")
    if i!=4:
        print((" ")*(10-2*i-3)+"*",end=" ")
    print()