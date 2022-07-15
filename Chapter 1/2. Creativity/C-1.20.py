# Python’s random module includes a function shuffle(data) that accepts a list of elements and randomly reorders the elements so that each possible order occurs with equal probability. The random module includes a more basic function randint(a, b) that returns a uniformly random integer from a to b (including both endpoints). Using only the randint function, implement your own version of the shuffle function.

import random

l = input("Enter space seperated sequence : ").split()

l_shuffle = l
random.shuffle(l_shuffle)
print(l_shuffle)

l_randint = [random.randint(0, len(l)-1)]
print(l_randint)

