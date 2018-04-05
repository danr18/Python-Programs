# three_dice.py: writes the sum of three random integers between 1 and 6, such
# as you might get when rolling three dice.

import random
import stdio

#Get three random numbers in variables
a = random.randrange(1,7)
b = random.randrange(1,7)
c = random.randrange(1,7)
sum = a+b+c
#Write sum of three random numbers
stdio.writeln(sum)
