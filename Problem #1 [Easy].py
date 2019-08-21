# Good morning! Here's your coding interview problem for today.
# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

# Innitial thoughts... using a nested for loop is the obvious solution,
# though there is almost certainly more efficient ways.
# The fact that it specifies 2 numbers only makes this easier maybe.
# Rather than n^2, I think I can at least get this to a n* log(n) solution
if __name__ == '__main__':
    collection_of_ints = list([10, 15, 3, 7])
    n = 17
    index_outer = 0
    for item in collection_of_ints:
        index_inner = 0
        for i in collection_of_ints[index_outer+1:]:
            if item + i == n:
                print(f"Value {item} at index {index_outer} + Value {i} at index {index_inner} = {n}.")
            index_inner += 1
        index_outer += 1


# reaction: Surprisingly I had issues using indexes in the for loops with lists of integers...
# There's probably a way since "for index, item in collection_of_ints" doesn't seem to work.
