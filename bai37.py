#!/usr/bin/python
def xoatrung(dictionary):
    i = 0
    val = dictionary.values()
    l = len(val)
    while (i < l-1):
        j = i + 1
        mark = 0
        while (j < l):
            if (val[i] == val[j]):
                del dictionary[dictionary.items()[j][0]]
                val.pop(j)
                mark = 1
                l = l - 1
                j -= 1
            j += 1
        if (mark == 1):
            del dictionary[dictionary.items()[i][0]]
            val.pop(i)
            l = l - 1
            i -= 1
        i += 1
    return dictionary
            
