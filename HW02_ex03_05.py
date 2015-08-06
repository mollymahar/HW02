#!/usr/bin/env python
# HW02_ex03_05

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the 
# value printed next appears on the same line.

# print '+', 
# print '-'

# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.

# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body
top = "+" + 4 * " -" + " "
middle = "|" + 9 * " "


def box(c):
	print top * c + "+"
	print middle * c + "|"
	print middle * c + "|"
	print middle * c + "|"
	print middle * c + "|"

def two_by_two():
	box(2)
	box(2)
	print top * 2 + "+"

def four_by_four():
	box(4)
	box(4)
	box(4)
	box(4)
	print top * 4 + "+"








# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    
    two_by_two()
    four_by_four()
    



if __name__ == "__main__":
    main()