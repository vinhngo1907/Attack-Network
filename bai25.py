#!/usr/bin/python
def daidien(list1):
    dsdaidien = list()
    for i in list1:
        if i not in dsdaidien:
            dsdaidien.append(i)
    return dsdaidien
