#!/usr/bin/python
import math
print 'Phuong trinh bac 2 dang a.x^2 + b.x + c = 0'
a = input('Nhap a: ')
b = input('Nhap b: ')
c = input('Nhap c: ')

if (a==0):
	if (b==0):
		if (c==0):
			print 'Phuong trinh co vo so nghiem'
		else:
			print 'Phuong trinh vo nghiem'
	else:
		if (c==0):
			print 'Phuong trinh co nghiem: x = 0'
		else:
			print 'Phuong trinh co nghiem: x = %g' %(float(-c)/b)
else:
	delta = b*b - 4*a*c
	if (delta<0):
		print 'Phuong trinh vo nghiem'
	elif (delta==0):
		print 'Phuong trinh co nghiem kep: x1 = x2 = %g' %(float(-b)/2*a)
	else:
		print 'Phuong trinh co 2 nghiem phan biet: x1 = %g, x2 = %g' %((-b + math.sqrt(delta))/float(2*a), (-b - math.sqrt(delta))/float(2*a))