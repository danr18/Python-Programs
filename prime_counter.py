# prime_counter.py: takes an integer N as command-line argument and writes the
# number of primes less than or equal to N.

import stdio
import sys
import stdarray

# Get N from command line, as an int.
N = int(sys.argv[1])

# Define primes to determine if number is prime.
primes = stdarray.create1D(N+1, True)

# Iterate over integers 2 to N (inclusive).
for i in range(2, N):
    if (primes[i]):
        for j in range(2, N // i + 1):
            primes[i*j] = False

number = 0

for i in range(2, N+1):
    if primes[i]:
        number += 1

# Write number of primes.
stdio.writeln(number)
