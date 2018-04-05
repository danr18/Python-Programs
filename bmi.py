# bmi.py: Takes two floats w (for weight) and h (for height) as command-line
# arguments and prints the body mass index (BMI), calculated as the ratio of
# the weight to the square of the height.

import stdio
import sys

#Get w from command line
w = float(sys.argv[1])

#Get h from commman line
h = float(sys.argv[2])

#Write BMI
h2 = h**2
bmi = w / h2
stdio.writeln(bmi)
