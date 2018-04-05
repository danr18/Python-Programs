# polar.py: Takes two floats x and y representing the Cartesian coordinates of
# a point as command-line arguments and prints the corresponding polar
# coordinates, calculated as r=(x^2+y^2)^0.5 and theta=arctan(y/x).

import math
import stdio
import sys

# Get x from command line
x = float(sys.argv[1])

# Get y from command line
y = float(sys.argv[2])

# Write value of r=(x^2+y^2)^0.5
x2 = x**2
y2 = y**2
r = (x2+y2)**(0.5)
stdio.writeln(r)
# Write value of theta=arctan(y/x)
theta = math.atan(y/x)
stdio.writeln(theta)
