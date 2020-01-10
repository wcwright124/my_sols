from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    RESCALE_FACTOR = 2

    def __init__(self, capacity):
        # TODO - you fill in here.
        self.__queue = [None] * capacity
        self.__size = 0
        self.__head = 0
        self.__tail = 0
        return

    def enqueue(self, x):
        # TODO - you fill in here.
        if self.__size == len(self.__queue): # resize condition
            self.__queue = self.__queue[self.__head:] + self.__queue[:self.__head] # shift over
            self.__head, self.__tail = 0, self.__size
            temp = [None] * ((Queue.RESCALE_FACTOR - 1) * self.__size)
            self.__queue += temp
        self.__queue[self.__tail] = x
        self.__tail = (self.__tail + 1) % len(self.__queue)
        self.__size += 1
        return

    def dequeue(self):
        # TODO - you fill in here.
        res = self.__queue[self.__head]
        self.__head = (self.__head + 1) % len(self.__queue)
        self.__size -= 1
        return res

    def size(self):
        # TODO - you fill in here.
        return self.__size


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
