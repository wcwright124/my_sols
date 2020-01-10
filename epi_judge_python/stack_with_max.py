from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    def __init__(self):
        self.__stack = []
        self.__max_stack = []
    
    def empty(self):
        # TODO - you fill in here.
        return len(self.__stack) == 0

    def max(self):
        # TODO - you fill in here.
        return self.__max_stack[-1][0]

    def pop(self):
        # TODO - you fill in here.
        max_idx = self.__max_stack[-1][1]
        pop_idx = len(self.__stack) - 1
        if pop_idx == max_idx:
            self.__max_stack.pop()
        return self.__stack.pop()

    def push(self, x):
        # TODO - you fill in here.
        if self.empty():
            self.__stack.append(x)
            self.__max_stack.append((x, 0))
        else:
            if x > self.max():
                self.__max_stack.append((x, len(self.__stack)))
            self.__stack.append(x)
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
