from test_framework import generic_test, test_utils

def generate_balanced_parentheses(num_pairs):
    def helper(num_left_needed, num_right_needed, prefix):
        if num_right_needed == 0:
            res.append(prefix)
            return
        if num_left_needed > 0:
            helper(num_left_needed-1, num_right_needed, prefix + '(')
        if num_left_needed < num_right_needed:
            helper(num_left_needed, num_right_needed-1, prefix + ')')
        return
    res = []
    helper(num_pairs, num_pairs, '')
    return res


def generate_balanced_parentheses2(num_pairs):
    def helper(n):
        if n == 0:
            results.append([''])
            return
        else:
            helper(n - 1)
            res = set()
            for p in results[-1]:
                res.add('(' + p + ')')
            for i in range(1, n):
                left = results[i]
                right = results[n - i]
                for x in left:
                    for y in right:
                        res.add(x + y)
            results.append(list(res))
    results = []
    helper(num_pairs)
    return results[-1]

def generate_balanced_parentheses1(num_pairs):
    def helper(n):
        if n == 0:
            return ['']
        elif n == 1:
            return ['()']
        else:
            res = set()
            previous_results = [helper(i) for i in range(n)]
            for p in previous_results[-1]:
                res.add('(' + p + ')')
            for i in range(1, n):
                left = previous_results[i]
                right = previous_results[n-i]
                for x in left:
                    for y in right:
                        res.add(x + y)
            return list(res)
    # TODO - you fill in here.
    return helper(num_pairs)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
