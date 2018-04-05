# random_integer.py: Takes two integers a and b from the command line and
# writes a random integer between a (inclusive) and b (exclusive).

import random
import stdio
import sys

# Get two numbers from command line
a = int(sys.argv[1])
b = int(sys.argv[2])
# Get a random integer between [a, b)
c = random.randrange(a,b)
# Write integer
stdio.writeln(c)
