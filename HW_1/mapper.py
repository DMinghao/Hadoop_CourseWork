#!/usr/bin/env python

import sys
from itertools import combinations 
 

#--- get all transactions from stdin ---
for transaction in sys.stdin:
    #--- remove leading and trailing whitespace---
    transaction = transaction.strip()

    #--- split the transaction into numbers ---
    numbers = map(lambda x : int(x), transaction.split())

    #--- get all possible combinations of transaction ---
    ans = combinations(numbers, 2)

    #--- output tuples ((item a, item b), 1) in tab-delimited format---
    for a in ans: 
        print("%s\t%s"%(a, 1))
