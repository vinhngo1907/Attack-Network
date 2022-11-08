#!/usr/bin/python
Chuoi = raw_input('Nhap chuoi cac so cach nhau boi dau \';\' : ')
Chuoi1 = Chuoi.split(';')
Tong = 0
for i in Chuoi1:
	Tong = Tong + int(i)
print 'Tong cac so da nhap la: %g' %float(Tong)
