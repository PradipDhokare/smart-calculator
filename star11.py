for i in range(0, 10):
    for j in range(0, 100):
        # Letter P
        if (j == 0 or (i == 0 and j < 5) or (i == 4 and j < 5) or (j == 5 and i < 4 and i > 0)):
            print("*", end="")

        # Letter R (starting at column 10)
        elif (j == 10 or (i == 0 and j > 10 and j < 16)
              or (i == 4 and j > 10 and j < 16)
              or (j == 16 and i > 0 and i < 4) or (i - j == -7 and i > 4)):
            print("*", end="")

        # Letter A (starting at column 20)
        elif (i + j == 29 or j - i == 29 or (i == 4 and j >= 25 and j <= 33)):
            print("*", end="")

        # Letter D (starting at column 48)
        elif (j == 47 or (i == 0 and j > 47 and j < 53)
              or (i == 9 and j > 47 and j < 53)
              or (j == 53 and i >= 1 and i <= 8)):
            print("*", end="")

        else:
            print(" ", end="")
    print()
