# wind_chill.py: Takes two floats t and v as command-line arguments and
# prints the wind chill w, calculated as w=35.74+0.6215t+(0.4275t-35.75)v^0.16.

import stdio
import sys

# Get t from command line
t = float(sys.argv[1])

# Get v from command line
v = float(sys.argv[2])

# Write value of w=35.74+0.6215t+(0.4275t-35.75)v^0.16
w = 35.74 + (0.6215*(t)) + ((0.4275*(t)) - (35.75))*((v)**(0.16))
stdio.writeln(w)
