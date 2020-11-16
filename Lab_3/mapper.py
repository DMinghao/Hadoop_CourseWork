#!/usr/bin/env python

import sys
for line in sys.stdin:
    line = line.strip()
    items = line.split()
    for item in items:
        print('(%s)\t%s' % (item,1))
