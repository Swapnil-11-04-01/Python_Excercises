# Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.

try:
    def minmax(data):
        min = data[0]
        max = data[0]
        for i in data:
            if i > max:
                max = i
            if i < min:
                min = i

        return min, max


    Input = input("Write space seperated list of numbers : ")
    data = list(map(lambda x: int(x), Input.split(" ")))
    out = minmax(data)
    print(out)

except ValueError:
    print("Please enter integer values only and avoid entering empty spaces")
    print("Values u passed : ", data)
