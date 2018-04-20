import stdio
import sys


# Return True if s is a palindrome and False otherwise. You may assume that
# s is all lower case and doesn't any whitespace characters.
def is_palindrome(s):
    #If the word is the same as the word reversed, it means it's a palindrome, so return True.
    #If it's not, return False
    if s == s[::-1]:
        return True
    else:
        return False


# Test client [DO NOT EDIT]. Reads a string s as command-line argument and
# prints True if s is a palindrome, ie, reads the same forwards and backwards,
# and False otherwise.
def _main():
    s = sys.argv[1]
    stdio.writeln(is_palindrome(s))


if __name__ == '__main__':
    _main()

