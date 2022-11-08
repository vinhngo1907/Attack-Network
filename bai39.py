#!/usr/bin/python
s = raw_input('Nhap ten file can doc: ')
f = open(s, 'r')
str = f.read()
print 'Noi dung file la: \n', str
f.close()
