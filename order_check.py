# order_check.py: Takes three floats values x, y, and z as command-line
# arguments and prints True if the values are strictly ascending or
# descending (i.e., x<y<z or x>y>z), and False otherwise.

import stdio
import sys

# Get x from command line
x = float(sys.argv[1])
# Get y from command line
y = float(sys.argv[2])
# Get z from command line
z = float(sys.argv[3])

if x<y<z or x>y>z:
    stdio.writeln("True")
else:
    stdio.writeln("False")
