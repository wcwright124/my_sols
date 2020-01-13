import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure


class LruCache:
    def __init__(self, capacity):
        # TODO - you fill in here.
        self.__cache = collections.OrderedDict()
        self.__capacity = capacity
        return

    def lookup(self, isbn):
        # TODO - you fill in here.
        if isbn in self.__cache:
            price = self.__cache.pop(isbn)
            self.__cache[isbn] = price
            return price
        return -1

    def insert(self, isbn, price):
        # TODO - you fill in here.
        if isbn in self.__cache:
            price = self.__cache.pop(isbn)
        elif len(self.__cache) == self.__capacity:
            self.__cache.popitem(last=False)
        self.__cache[isbn] = price
        return

    def erase(self, isbn):
        # TODO - you fill in here.
        if isbn in self.__cache:
            del self.__cache[isbn]
            return True
        return False


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
