# min_max.py: reads in floats (as many as the user enters) from standard
# input and writes out the minimum and maximum values along with their ranks,
# ie, their positions (starting at 1) in the input.

import stdio

# Read floats from standard input into a list b.
a = raw_input()
b = a.split()
b = [float(x) for x in b]


# Iterate the list b to identify the minimum value and its rank and the
# maximum value and its rank.

c = sorted(b)
min_val = min(c)
max_val = max(c)
min_rank = b.index(min_val) + 1
max_rank = b.index(max_val) + 1

# Write the results (min_val, min_rank, max_val, max_rank).
stdio.writef('min val = %f, min rank = %d\n', min_val, min_rank)
stdio.writef('max val = %f, max rank = %d\n', max_val, max_rank)
