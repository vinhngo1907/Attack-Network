#!/usr/bin/python
def chuoinhiphan(n):
        m = 2**n
        i = 0
        while (i<=m-1):
        	temp = bin(i)[2:].zfill(n)
        	i += 1
        	print temp
