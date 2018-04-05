# three_sort.py: Takes three integers as command-line arguments and prints
# them in ascending order, separated by spaces.

import stdio
import sys

# Get three numbers from command line
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
#Save values in a variable as a sorted list
three = sorted([a,b,c])
#Write the three values sorted
stdio.writeln(str(min(three)) + " " + str(three[1]) + " " + str(max(three)))



