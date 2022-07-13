# Write a short Python function, is_multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.

try:
    def is_multiple(n, m):
        return True if n%m == 0 else False

    n= int(input("n = "))
    m =int(input("m = "))
    out = is_multiple(n, m)
    print(out)

except ZeroDivisionError:
    print(f"Can,t divide {n} by 0.")

