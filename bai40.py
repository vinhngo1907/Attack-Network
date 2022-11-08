#!/usr/bin/python
s = raw_input('Nhap ten file can doc: ')
n = input('Nhap so dong can doc: ')
f = open(s, 'r')
print 'Noi dung file la: \n'
for i in range(n):
    l = f.next().strip()
    print l
f.close()
