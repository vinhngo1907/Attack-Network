#!/usr/bin/python
Chuoi = raw_input('Nhap chuoi moi: ')
Chuoi = str(Chuoi)
Chuoi = ''.join(Chuoi.split())
Danhsach = list(Chuoi)
Ketqua = dict()
for kytu in Danhsach:
	if kytu not in Ketqua.keys():
		Ketqua[kytu] = Danhsach.count(kytu)
print 'Tan so xuat hien cac ky tu trong chuoi la: %s' %Ketqua