# Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order than they were before, and compare this method to an equivalent Python function for doing the same thing.

Input = input("Enter space seperated list of numbers : ")
l = Input.split()
l = list(map(lambda x : int(x), l))
print("Original List : ", l)

for i, j in zip(range(0, len(l)//2 + 1), range(len(l) - 1, len(l)//2 - 1, -1)):
    if i == j:
        break
    l[i] += l[j]
    l[j] = l[i] - l[j]
    l[i] = l[i] - l[j]

print("Updated List  : ", l)
