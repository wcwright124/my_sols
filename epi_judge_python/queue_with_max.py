import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure


class QueueWithMax:
    def __init__(self):
        self.__queue = collections.deque()
        self.__max = collections.deque()
    
    def enqueue(self, x):
        # TODO - you fill in here.
        self.__queue.append(x)
        while self.__max and self.__max[-1] < x:
            self.__max.pop()
        self.__max.append(x)
        return

    def dequeue(self):
        # TODO - you fill in here.
        if self.__max[0] == self.__queue[0]:
            self.__max.popleft()
        return self.__queue.popleft()

    def max(self):
        # TODO - you fill in here.
        return self.__max[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_with_max.py",
                                       'queue_with_max.tsv', queue_tester))
