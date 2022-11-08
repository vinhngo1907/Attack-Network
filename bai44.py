#!/usr/bin/python
s = raw_input('Nhap ten file can dem: ')
f = open(s, 'r')
dictcount = dict()
for word in f.read().split():
    if word not in dictcount:
        dictcount[word] = 1
    else:
        dictcount[word] += 1
print dictcount
