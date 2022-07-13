#  Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the same element?

Input = input("Enter any string : ")

n = len(Input)
print(f"length of string is : {n}")

for k, j in zip(range(-n, 0), range(0, n)):
    if Input[k] == Input[j]:
        print(f"'j' = {j} is the equivalent index to 'k' = {k} index, i.e 'j' must be equal to 'k' + length of string")
