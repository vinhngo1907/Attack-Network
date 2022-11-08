#!/usr/bin/python
ds = raw_input('Nhap cac gia tri cua danh sach cach nhau boi dau \';\': ')
ds1 = ds.split(';')
i = 0
temp = list()
for i in ds1:
        if (float(i).is_integer()):
                temp.append(int(i))
        else:
                temp.append(float(i))
ds2 = sorted(temp)
ds3 = sorted(temp, reverse=True)
print 'Danh sach tang dan: %s' %ds2
print 'Danh sach giam dan: %s' %ds3
