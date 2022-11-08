#!/usr/bin/python
s = raw_input('Nhap ten file can doc: ')
n = input('Nhap so dong cuoi can doc: ')
fo = open(s, 'r')
f = fo.readlines()
print 'Noi dung file la: \n'
i = len(f) - n
while (i < len(f)):
    print f[i].strip()
    i += 1
fo.close()
