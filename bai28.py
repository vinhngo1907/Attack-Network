#!/usr/bin/python
import math
def median(data): #trung vi
	data = sorted(data)
	n = len(data)
	if (n%2 == 1):
		return data[n//2]
	else:
		i = n//2
		return (data[i-1] + data[i])/2

def mean(data): #trung binh
	return sum(data)/len(data)

def variance(data): #phuong sai
	u = mean(data)
	return sum([(i-u)**2 for i in data])/len(data)

def stddev(data): #standard deviation: do lech chuan
	return math.sqrt(variance(data))

	
