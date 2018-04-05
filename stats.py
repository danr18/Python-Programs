# stats.py: writes the mean, variance, and standard deviation of
# the floats x_1, x_2, \dots, x_n supplied as command-line
# arguments.

import stdio
import sys

# Create a list a consisting of the floats from the command line.
a = [float(x) for x in sys.argv[1:]]

# Define a variable n and set it to the number of elements in a.
n = len(a)

# Compute the average of a into a variable avg.
avg = sum(a) / n

# Compute the variance of a into a variable var.
var = 0
for v in a:
    var += ((v - avg) ** 2) / n

# Compute the standard deviation of a into a variable std.
std = var ** 0.5

# Write avg, var, and std.
stdio.writeln(avg)
stdio.writeln(var)
stdio.writeln(std)
