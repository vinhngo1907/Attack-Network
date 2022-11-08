#!/usr/bin/python
s = raw_input('Nhap chuoi can kiem tra: ')
s1 = ''.join(reversed(s))
if (s1 == s):
	print 'Chuoi \'%s\' la chuoi doi xung.' %s
else:
	print 'Chuoi \'%s\' khong doi xung.' %s
