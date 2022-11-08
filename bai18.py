#!/usr/bin/python
def xoa(data):
    test = list()
    for i in data:
        if (i not in test):
            test.append(i)
    return test
