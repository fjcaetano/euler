__author__ = 'flaviocaetano'

import json

from datetime import datetime


def name_list():
    with open('names.txt', 'r') as file:
        return json.loads(file.read())


def main():
    sorted_names = sorted(name_list())

    for i, name in enumerate(sorted_names, start=1):
        name_value = sum(map(lambda x: ord(x)-96, name.lower()))

        yield i * name_value


if __name__ == '__main__':
    t0 = datetime.now()

    result = sum(main())

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)
