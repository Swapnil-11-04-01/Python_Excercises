#  Write a short Python function that takes a positive integer n and returns, the sum of the squares of all the odd positive integers smaller than n.


def sum_of_square_of_all_smaller_odd_int(n):
    sum = 0
    for i in range(1, n):
        if i%2 != 0:
            sum += i**2
    return sum


n = int(input("ENter number : "))
out = sum_of_square_of_all_smaller_odd_int(n)
print(out)