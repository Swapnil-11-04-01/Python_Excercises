#  Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.

def distinct_pairs(seq):
    dict = {}
    for i in seq:
        for j in seq:
            if i == j:
                continue
            if (j, i) not in dict.keys() and i*j%2 == 1:
                dict[(i, j)] = i*j

    return dict

Input = list(map(lambda x : int(x), input("Enter sequence of space seperated numbers : ").split()))
out = distinct_pairs(Input)
print(out)
print("These", len(out), "pairs are present in your sequence havinf an odd product.")