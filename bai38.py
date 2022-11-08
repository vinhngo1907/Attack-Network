#!/usr/bin/python
class SinhVien:

    def __init__(self, hoten, gioitinh = 'Nam'):
        self.hoten = hoten
        self.gioitinh = gioitinh

    def diemdanh(self):
        print 'Toi la sinh vien'

    def thongtin(self):
        print 'Ho ten: ',self.hoten
        print 'Gioi tinh: ',self.gioitinh
        
class SinhVienCNTT(SinhVien):
    def diemdanh(self):
        print 'Toi la sinh vien CNTT'

class SinhVienTTMMT(SinhVien):
    def diemdanh(self):
        print 'Toi la sinh vien TT-MMT'
