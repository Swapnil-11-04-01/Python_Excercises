# Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.

def is_even(k):
    digit = (k & (1 << 0)) >> 0
    return True if digit == 0 else False


k = int(input("k = "))
out = is_even(k)
print(out)
