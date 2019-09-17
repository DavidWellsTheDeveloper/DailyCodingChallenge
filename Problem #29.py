# Good morning! Here's your coding interview problem for today.
# This problem was asked by Amazon.
# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated
# successive characters as a single count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists
# solely of alphabetic characters. You can assume the string to be decoded is valid.

# Very easy problem if I wanted to go back and improve it with "invalid" input handling that might make it more
# interesting.


class CodedString:
    def __init__(self, raw_string):
        self.raw_string = raw_string
        self.encoded_string = self.encode()

    def encode(self):
        last_char = None
        count = 0
        self.encoded_string = ""
        for char in self.raw_string:
            if last_char is not None and char != last_char:
                self.encoded_string += str(count) + last_char
                count = 1
                last_char = char
            else:
                count += 1
                last_char = char
        self.encoded_string += str(count) + last_char
        return self.encoded_string

    def decode(self):
        self.raw_string = ""
        count = None
        for val in self.encoded_string:
            if val.isdigit():
                count = int(val)
            else:
                for i in range(0, count):
                    self.raw_string += val
        return self.raw_string


if __name__ == '__main__':
    codedString = CodedString("AAAABBBCCDAA")
    print(codedString.encoded_string)
    print(codedString.decode())
