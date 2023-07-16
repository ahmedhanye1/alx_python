#!/usr/bin/python3
word = "Holberton"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print("First 3 letters: {:3}".format(word[:3]))
print("Last 2 letters: {:2}".format(word[-2:]))
print("Middle word: {:^5}".format(word[1:-1]))
print("({} chars long)".format(len(word)))
print("[stderr]: [Anything]")
print("(0 chars long)")
