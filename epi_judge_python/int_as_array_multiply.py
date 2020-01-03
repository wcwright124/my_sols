from test_framework import generic_test


def multiply(num1, num2):
    # TODO - you fill in here.
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    res = [0] * (len(num1) + len(num2))
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])
    for i in range(len(num1)-1, -1, -1):
        for j in range(len(num2)-1, -1, -1):
            res[i + j + 1] += num1[i] * num2[j]
            res[i + j] += (res[i + j + 1] // 10)
            res[i + j + 1] %= 10
    while len(res) > 1 and res[0] == 0:
        del res[0]
    if sign == -1:
        res[0] = -res[0]
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
