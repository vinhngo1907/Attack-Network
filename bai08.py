#!/usr/bin/python
Chuoi = raw_input('Nhap vao 1 chuoi: ')
print 'Do dai cua chuoi vua nhap la: %d' %len(Chuoi)
print 'Ky tu dau tien cua chuoi la: %c' %Chuoi[0]
print 'Ky tu cuoi cung cua chuoi la: %c' %Chuoi[-1]
print 'In ky tu tu vi tri i den vi tri j'
i = int(input('Nhap vi tri bat dau: i= '))
j = int(input('Nhap vi tri ket thuc: j= '))
j = j + 1
print 'Noi dung chuoi duoc in la: %s' %Chuoi[i:j]