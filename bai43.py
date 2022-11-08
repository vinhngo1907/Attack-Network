#!/usr/bin/python
s = raw_input('Nhap ten file can dem: ')
f = open(s, 'r')
sumword = 0
for word in f.read().split():
    sumword += 1
f.seek(0)
sumline = sum(1 for line in f)
print 'Tong so tu la: ', sumword
print 'Tong so dong la: ', sumline
f.close()
