#  Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).

def distinct_numbers(seq):
    for i in range(0, len(seq) - 1):
        if seq[i] in seq[i + 1:]:
            print("All numbers are not distinct.")
            return 0

    print("All numbers are distinct.")


seq = list(map(lambda x: int(x), input("Enter sequence of space seperated numbers : ").split()))
distinct_numbers(seq)
