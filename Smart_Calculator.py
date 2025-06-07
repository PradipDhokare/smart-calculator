import sys
sys.path.append("F:\\Coding Sikho Python Classs")  # Add folder, not file
from Calculator_Functions import *

print(responses[0])
print(responses[1])

while True:
    t1 = input("Please Ask: ").upper()

    # Check if it's a known command
    found = False
    for key in operations:
        if key in t1:
            func = operations[key]
            nums = extract_num(t1)
            try:
                # Single-argument functions
                if key in ["FACTORIAL", "SIN", "COSIN", "TAN", "LOG",
                           "CELSIUS TO FAHRENHEIT", "FAHRENHEIT TO CELSIUS",
                           "C TO F", "F TO C", "PRIME", "EVEN"]:
                    r = func(nums[0])
                else:
                    r = func(nums[0], nums[1])
                print("→", r)
            except:
                print("❌ Please ask a correct question with valid numbers.")
            found = True
            break

    # Check if it's a special command like "AMIT" or "BYE"
    if not found:
        for cmd in commands:
            if cmd in t1:
                commands[cmd]()
                found = True
                break

    # If nothing matches
    if not found:
        print(responses[4])
        print(responses[5])
