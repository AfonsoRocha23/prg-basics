###
# A program that generates a random number between 5 and 10 
# five times using a loop.
#
import random

for i in range(5):
    random_number = random.randint(5, 10)
    print(random_number)