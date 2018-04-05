import stdio
import sys

# Get x0 from command line, as a float.
x0 = float(sys.argv[1])

# Get v0 from command line, as a float.
v0 = float(sys.argv[2])

# Get t from command line, as a float.
t = float(sys.argv[3])

# Declare g = 9.78033.
g = 9.78033

# Write the value of x0 + v0t - gt^2/2.
operationv = v0 * t
operationt = t ** 2
operationg = (g * operationt) / 2
stdio.writeln(x0 + operationv - operationg)
