# Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the built-in sum function.

print(sum(i*i for i in range(1, int(input("Enter number : "))) if i%2 != 0))