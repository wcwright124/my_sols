from test_framework import generic_test

def convert_base(num_as_string, b1, b2):
    # TODO - you fill in here.
    if num_as_string[0] == '-':
        return '-' + convert_base(num_as_string[1:], b1, b2)
    # convert into a decimal
    num = 0
    for c in num_as_string:
        num *= b1
        if c.isalpha():
            num += 10 + ord(c) - ord('A')
        else:
            num += ord(c) - ord('0')
    if num == 0:
        return '0'
    # convert decimal to base b2
    vals = ['A', 'B', 'C', 'D', 'E', 'F']
    res = []
    while num:
        current_digit = num % b2
        if current_digit <= 9:
            res.append(str(current_digit))
        else:
            res.append(vals[current_digit - 10])
        num //= b2
    res.reverse()
    return ''.join(res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
