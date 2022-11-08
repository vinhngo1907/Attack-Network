#!/usr/bin/python
n = input('Nhap so nguyen duong: n = ')

#S = 1 + 2 + ... +n
S = 0
i = 1
while (i<=n):
	S = S + i
	i = i + 1
print 'S = 1 + 2 + ... + %d = %d' %(n, S)

#S1 = 1 + 3 + ... + (2n-1)
S1 = 0
i = 1
while (i<=2*n-1) :
	S1 = S1 + i
	i = i + 2
print 'S1 = 1 + 3 + ... + %d = %d' %(2*n-1, S1)

#S2 = 2 + 4 + ... + 2n
S2 = 0
i = 2
while (i<=2*n):
	S2 = S2 + i
	i = i + 2
print 'S2 = 2 + 4 + ... + %d = %d' %(2*n, S2)

#S3 = 1 + 2^2 + ... + n^2
S3 = 0
i = 1
j = 0
while (i<=n**2):
	S3 = S3 + i
	j = j + 1
	i = i + 2*j +1 
print 'S3 = 1 + 2^2 + ... + %d = %d' %(n**2, S3)

#S4 = 1 + 1/2 + ... + 1/2^n
S4 = 0.0
i = 1
j = 0
while (i>=float(1)/2**n):
	S4 = S4 + i
	j = j + 1
	i = float(1)/2**j
print 'S4 = 1 + 1/2 + ... + %g = %g' %(float(1)/2**n, S4)