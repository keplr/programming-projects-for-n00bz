#!/usr/bin/env python3
#
# If odd: 3n +1
# If even: n / 2
# It always finds 1.

while True:
    try:
        natNum = int(input("Starting number: "))
        break
    except ValueError:
        print("Please enter a whole integer.")

while True:
    if natNum % 2 == 0:
            natNum = natNum / 2
    elif natNum == 1:
        break
    else:
        natNum = (natNum * 3) + 1
    print(natNum)
