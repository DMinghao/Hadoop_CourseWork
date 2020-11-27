#!/usr/bin/env python
import sys
 
# maps combinations to their counts
combinationCount = {}
SUPPORT = 2
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    key, value = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        value = int(value)
    except ValueError:
        continue

    #short hand operation to assign or add value 
    combinationCount[key] = key in combinationCount and combinationCount[key] + value or value
 
# write the tuples to stdout
# Note: they are unsorted
for key in combinationCount.keys():
    if combinationCount[key] >= SUPPORT: 
        print("%s\t%s"%(key, combinationCount[key]))
