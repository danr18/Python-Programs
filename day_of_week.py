# day_of_week.py: Takes three integers m (for month), d (for day), and y
# (for year) as command-line arguments and prints the day of the week (0 for
# Sunday, 1 for Monday, and so on) D, calculated as follows:
#
# y0 = y - (14 - m) / 12
# x0 = y0 + y0 / 4 - y0 / 100 + y0 / 400
# m0 = m + 12 * ((14 - m) / 12) - 2
# D = (d + x0 + 31 * m0 / 12) % 7

import stdio
import sys

# Get m (month) from command line
m = int(sys.argv[1])
# Get d (day) from command line
d = int(sys.argv[2])
# Get y (year) from command line
y = int(sys.argv[3])

# Write values
y0 = y - (14 - m) / 12
x0 = y0 + y0 / 4 - y0 / 100 + y0 / 400
m0 = m + 12 * ((14 - m) / 12) - 2
D = (d + x0 + 31 * m0 / 12) % 7
stdio.writeln(D)
