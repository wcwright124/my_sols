from test_framework import generic_test


def evaluate(expression):
    def helper(a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a // b
    # TODO - you fill in here.
    OPS = set(['+', '-', '/', '*'])
    expression_list = expression.split(',')
    stack = []
    for e in expression_list:
        if e in OPS:
            b = stack.pop()
            a = stack.pop()
            res = helper(a, b, e)
            stack.append(res)
        else: # is integer
            stack.append(int(e))
    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
