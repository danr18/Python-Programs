# missing.py: takes an integer N as command-line argument, reads in N - 1
# distinct integers between 1 and N from standard input, and writes the
# missing number.

import stdarray
import stdio
import sys

# Get N from command line, as an int.
N = int(sys.argv[1])

# Define a list a of N + 1 booleans, with each element initialized to False.
a = range(1,N+1)


# Read N - 1 distinct integers between 1 and N from standard input, and
# for each such integer x, set a[x] to True, meaning x was found.
b = raw_input()
c = b.split()
c = [int(x) for x in c]

d = set(c)
different = [i for i in a if not i in d]


# Iterate over a[1:] and write index of the False element, since that is the
# missing number.
stdio.writeln(different[0])


    
