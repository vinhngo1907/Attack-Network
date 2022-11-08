#!/usr/bin/python
def thapHaNoi(n, cotA, cotC, cotB):
	if (n == 1):
		print 'Chuyen', cotA, 'sang', cotB
	else:
		thapHaNoi(n-1, cotA, cotB, cotC)
		print 'Chuyen', cotA, 'sang', cotB
		thapHaNoi(n-1, cotC, cotA, cotB)
