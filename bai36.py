#!/usr/bin/python
def combine(dict1, dict2):
    result = dict(dict1, **dict2)
    i = 0
    while (i < len(dict1)):
        j = 0
        while (j < len(dict2)):
            if (dict1.keys()[i] == dict2.keys()[j]):
                result.update({dict1.keys()[i]:(dict1.values()[i]+dict2.values()[j])})
            j += 1
        i += 1
    return result
