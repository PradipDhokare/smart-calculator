import sys
print(sys.path.append("F:\\Coding Sikho Python Classs\\Calculator_Functions.py"))  # use double slashes
from Calculator_Functions import *
print(responses[0])
print(responses[1])

while True:
    t1 = input("Please Ask: ")
    for w in t1.split():
        w_upper = w.upper()
        if w_upper in operations.keys():
            func = operations[w_upper]
            l1 = extract_num(t1)
            try:
                if w_upper in ["FACTORIAL", "SIN", "COSIN", "TAN","LOG",
                               "CELSIUS TO FAHRENHEIT","FAHRENHEIT TO CELSIUS",
                               "C TO F","F TO C","PRIME","EVEN"]:
                    r = func(l1[0])
                else:
                    r = func(l1[0], l1[1])
                print(r)
            except:
                print("Please ask Correct Question")
            break

        elif w_upper in commands.keys():
            commands[w_upper]()
            break
    else:
        print(responses[4])
        print(responses[5])
