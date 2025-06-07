for i in range(0, 10):
    for j in range(0, 100):
        # Letter P
        if (j == 0 or (i == 0 and j < 5) or (i == 4 and j < 5) or (j == 5 and i < 4 and i>0)):
            print("*", end="")

        # Letter R (starting at column 10)
        elif (j == 10 or (i == 0 and j > 10 and j < 16) or (i == 4 and j > 10 and j < 16)
              or (j == 16 and i > 0 and i < 4) or (i - j == -7 and i > 4)):
            print("*", end="")

        # Letter A (starting at column 20)
        elif (i+j==29 or j-i==29 or (i==4 and j>=25 and j <=33)):
            print("*", end="")

        # Letter G (starting at column 48)
        elif ((i==0 and j>=48 and j<=58)or j==48 or (i==9 and j>=48 and j<=58) or (i==5 and j>=55 and j<=64)or (j==58 and i>5)):
            print("*", end="")

         # Letter T (starting at column 70)
        elif ((i==0 and j>=68 and j<=78)or j==73 ):
            print("*", end="")

        # Letter i (starting at column 80)
        elif (j == 85 or (i==0 and j>=80 and j<=90) or (i==9 and j>=80 and j<=90)):
            print("*", end="")

       


        else:
             print(" ", end="")
    print()
