#!/usr/bin/env python3

import multiprocessing # TODO: Multithreading
import random
import re
import sys
import urllib.request

regex = r'^[A-Za-z_.]+$'

countFore = 1
countLast = 1

cleanForeList = []
cleanLastList = []

try:
    uncleanLastList = urllib.request.urlopen(
        "http://www.census.gov/genealogy/www/data/1990surnames/dist.all.last"
    ).read().split()

    uncleanForeList = urllib.request.urlopen(
        "http://deron.meranda.us/data/census-derived-all-first.txt"
    ).read().split()
except MemoryError:
    print("Out of memory error.")
    sys.exit(0)


# The following takes a long time. TODO: Write names to Database
for i in range(0, len(uncleanForeList)):
    x = uncleanForeList[i].decode('utf-8')
    if re.match(regex, x):
        cleanForeList.append(x)
        print("Storing First Name:", x + ",",
            "Number:", countFore
        )
        countFore += 1

for i in range(0, len(uncleanLastList)):
    x = uncleanLastList[i].decode('utf-8')
    if re.match(regex, x):
        cleanLastList.append(x)
        print("Storing Last Name:", x + ",",
            "Number:", countLast
        )
    countLast += 1
print("\n")

for i in range(0, 10): # Second number is amount of names to generate.
    print(
        cleanForeList[random.randint(0, len(cleanForeList) - 1)].lower().title(),
        cleanLastList[random.randint(0, len(cleanLastList) - 1)].lower().title(),
    )
