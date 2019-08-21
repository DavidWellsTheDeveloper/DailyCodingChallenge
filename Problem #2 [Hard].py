# Good morning! Here's your coding interview problem for today.
# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is the product of
# all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

def get_product(in_list):
    product = 1
    for item in in_list:
        product *= item
    return product

def output_list_division(product, in_list):
    for index, item in enumerate(in_list):
        in_list[index] = product/item
    return in_list


# Initial thoughts... Division is the easiest and I will first implement that...
# To implement this without division you would probably need an n*log(n) solution at least.
if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5]
    print(output_list_division(get_product(input_list), input_list))

# after thoughts: I learned from the first problem and figured out the enumerate method of looping to get indexes.
# I put a bit more effort into this by actually refactoring methods rather than main.
