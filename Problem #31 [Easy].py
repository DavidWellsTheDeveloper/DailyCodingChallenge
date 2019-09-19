# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# The edit distance between two strings refers to the minimum number of character insertions,
# deletions, and substitutions required to change one string to the other. For example,
# the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”,
# substitute the “e” for “i”, and append a “g”.
# Given two strings, compute the edit distance between them.

# took less than 5 minutes. Easy.


def get_distance_between(string1, string2):
    count = 0
    if string2 > string1:
        # swap strings
        s = string1
        string1 = string2
        string2 = s
    for i in range(0, len(string1)):
        if len(string2) <= i:
            count += 1
        elif string1[i] != string2[i]:
            count += 1
    return count


if __name__ == '__main__':
    print(get_distance_between("kitten", "sitting"))
