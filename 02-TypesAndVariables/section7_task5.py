###
# A program that checks if a tree can be cut down based on its circumference.
# A tree can be cut down if its diameter is at least 50 cm.
#
import math

circumference = float(input('Enter tree circumference in cm: '))
diameter = circumference / math.pi
can_be_cut = diameter >= 50

print(f'Tree can be cut down: {can_be_cut}')
