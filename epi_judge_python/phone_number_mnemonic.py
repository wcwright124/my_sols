from test_framework import generic_test, test_utils

MAP = {0: '0', 1: '1', 2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9:'WXYZ'}


def phone_mnemonic(phone_number):
    def phone_mnemonic_helper(i):
        if i == len(phone_number):
            res.append(''.join(partial))
            return
        for c in MAP[int(phone_number[i])]:
            partial[i] = c
            phone_mnemonic_helper(i+1)
    # TODO - you fill in here.
    res = []
    partial = ['-'] * len(phone_number)
    phone_mnemonic_helper(0)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
