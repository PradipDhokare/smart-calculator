
for i in range(1,6):
    for j in range(1,10):
        if j>=6-i and j<=4+i and j%2==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
