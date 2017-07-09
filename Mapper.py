#!/usr/bin/python
#Reference: http://rare-chiller-615.appspot.com/mr1.html

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    if len(line) > 0:
        qdate = line[0].split('T')
        mag = line[4]
        print '%s\t%s' % (line[0].split('T')[0], line[4])



