#!/usr/bin/python
def dem(chuoicon, chuoi):
	ketqua = 0
	lencon = len(chuoicon)
	for i in range(len(chuoi)-lencon+1):
		if (chuoi[i:i+lencon] == chuoicon):
			ketqua += 1
	return ketqua
