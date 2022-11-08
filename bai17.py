#!/usr/bin/python
def merge(list1, list2):
	list3 = sorted(list1) + sorted(list2)
	print 'Danh sach tang dan: %s' %sorted(list3)
	print 'Danh sach giam dan: %s' %sorted(list3, reverse=True)
	