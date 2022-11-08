#!/usr/bin/python
s = raw_input('Nhap ten file can ghi: ')
f = open(s, 'a')
st = raw_input('Nhap chuoi can noi: \n')
f.write(st)
f.close()
