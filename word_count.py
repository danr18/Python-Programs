# word_count.py: reads text from standard input and writes to standard output
# the number of words in the text.

import stdio

#Get input from user and save it to a variable a
a = raw_input()
#Get the number of words from the input a
b = len(a.split())
#Write the number of words
stdio.writeln("Number of words = " + str(b))
