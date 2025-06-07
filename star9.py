for i in  range(1,5):
        for j in range(1,8):
            if j>=6-i and j<=4+i:
                print("*",end="")
            else:
                print(" ",end="")
    
        print()
n=4       
for i in  range(n-1,0,-1):
        for j in range(n-i):
           print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
    
        print()          
