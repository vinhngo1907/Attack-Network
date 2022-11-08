#!/usr/bin/python
def multivalue(dictionary):
    i = 0
    tich = 1
    while (i < len(dictionary)):
        tich = tich*dictionary.values()[i]
        i = i + 1
    return tich
