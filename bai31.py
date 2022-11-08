#!/usr/bin/python
def sumvalue(dictionary):
    i = 0
    tong = 0
    while (i < len(dictionary)):
        tong = tong + dictionary.values()[i]
        i = i + 1
    return tong
