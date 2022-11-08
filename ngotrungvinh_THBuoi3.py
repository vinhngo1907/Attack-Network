#Ngo Trung Vinh
#MSSV: B1709321
#Cau 1
class human:
	"""docstring for ClassName"""
	def __init__(self, hoten, namsinh,quequan,nghenghiep):
		# super(ClassName, self).__init__()
		self.hoten = hoten
		self.namsinh = namsinh
		self.quequan = quequan
		self.nghenghiep = nghenghiep
	def live(self,noicutru):
		return "Nguoi do ten {} dang song o {}".format(self.hoten,noicutru)
	def work(self, diachicoquan):
		return "Nguoi do ten {} dang lam nghe {} tai {}".format(self.hoten,self.nghenghiep,diachicoquan)

tranvana = human("Tran Van A", 1999, "Can Tho", "bac si")
print(tranvana.live("Can Tho")) 
print(tranvana.work("Benh vien da khoa"))

#Cau 2
n = int(input("Nhap so luong nguoi: n = "))
for i in range(n):
	hoten= input("Nhap ho ten nguoi thu %d: "%(i+1))
	namsinh= int(input("Nhap nam sinh nguoi thu %d: "%(i+1)))
	quequan= input("Nhap que quan nguoi thu %d: "%(i+1))
	nghenghiep= input("Nhap nghe nghiep nguoi thu %d: "%(i+1))
	person = human(hoten,namsinh,quequan,nghenghiep)
	print(person)
	diachicoquan = input("Nhap noi lam viec nguoi thu %d: "%(i+1))
	print(person.work(diachicoquan))

#Cau 3
class student(human):
	def __init__(self,hoten,namsinh,quequan,nghenghiep,MSSV,nganhhoc,DTB):
		super().__init__(hoten,namsinh,quequan,nghenghiep)
		self.nghenghiep = "sinh vien"
		self.MSSV = MSSV
		self.nganhhoc = nganhhoc
		self.DTB = DTB

	def __repr__(self):
		return "{} sinh nam {}  {} nghe nghiep {} co {} thuoc {}, ĐTB = {} \n".format(self.hoten,self.namsinh,self.quequan,self.nghenghiep,self.MSSV,self.nganhhoc,self.DTB)

	def study(self, Class):
		return "Sinh vien {} co MSSV {} thuoc nganh {} dang hoc tai phong {}".format(self.hoten,self.MSSV,self.nganhhoc,Class)
		
	def rank(self):
		loai = ""
		if self.DTB < 4:
			loai = "Loai yeu"
		elif self.DTB >= 4 and self.DTB < 6:
			loai = "Loai trung binh"
		elif self.DTB >=6 and self.DTB < 8:
			loai = "Loai kha"
		else:
			loai = "Loai gioi"
		return "Sinh vien {} co {} voi diem trung binh {} duoc xep loai {}".format(self.hoten,self.MSSV,self.DTB,loai)	

#Cau 4
SV1 = student("Lê Văn An", 2005, "quê Vĩnh Long", "sinh viên", 12345, "ngành CNTT", 7.6)
SV2 = student("Trần Văn Bình", 2007, "quê Trà Vinh","bac si", "56789", "Ngành Tài chính ngân hàng", 4.5)
print(SV1,SV1.rank())
print(SV2,SV2.rank())	 

#Cau 5
def nhapSV():
	hoten = input("Nhap ho ten: ")
	namsinh = input("Nhap nam sinh: ")
	quequan = input("Nhap que qua: ")
	nghenghiep = "sinh vien"
	MSSV = input("Nhap MSSV: ")
	nganhhoc = input("Nhap nganh hoc: ")
	DTB = float(input("Nhap diem trung binh: "))
	while(hoten):
		if(len(hoten) > 25):
			hoten = input("Ho ten co do dai khong qua 25 ki tu!\nMoi nhap lai: ")
		else:
			break	
	while(namsinh):
		if(len(namsinh) != 4 or namsinh.isnumeric() == False):
			namsinh = (input("Nam sinh phai co 4 chu so,\nMoi nhap lai: "))
		else:
			break
	while(quequan):
		if(len(quequan) > 50):
			quequan = input("Que quan phai co do dai khong qua 50,\nMoi nhap lai: ")
		else:
			break

	while(MSSV):
		if(len(MSSV) != 5 or MSSV.isnumeric() == False):
			MSSV = input("MSSV phai chua toi da 5 ky tu so,\nMoi nhap lai: ")
		else:
			break
	while(nganhhoc):	
		if(len(nganhhoc) > 40):
			nganhhoc = input("nganh hoc co do dai khong qua 40\nMoi nhap lai: ")	
		else:
			break
	while(DTB):	
		if(DTB <= 0 or DTB > 10):
			DTB = float(input("ĐTB > 0 and < 10,\nMoi nhap lai: "))
		else:
			break	
nhapSV()
#Cau 6
dsSV = []
def nhapSV():
	hoten = input("Nhap ho ten: ")
	namsinh = input("Nhap nam sinh: ")
	quequan = input("Nhap que quan: ")
	nghenghiep = "sinh vien"
	MSSV = input("Nhap MSSV: ")
	nganhhoc = input("Nhap nganh hoc: ")
	DTB = float(input("Nhap diem trung binh: "))
	while(hoten):
		if(len(hoten) > 25):
			hoten = input("Ho ten co do dai khong qua 25 ki tu!\nMoi nhap lai: ")
		else:
			break	
	while(namsinh):
		if(len(namsinh) != 4 or namsinh.isnumeric() == False):
			namsinh = (input("Nam sinh phai co 4 chu so,\nMoi nhap lai: "))
		else:
			break
	while(quequan):
		if(len(quequan) > 50):
			quequan = input("Que quan phai co do dai khong qua 50,\nMoi nhap lai: ")
		else:
			break

	while(MSSV):
		if(len(MSSV) != 5 or MSSV.isnumeric() == False):
			MSSV = input("MSSV phai chua toi da 5 ky tu so,\nMoi nhap lai: ")
		else:
			break
	while(nganhhoc):	
		if(len(nganhhoc) > 40):
			nganhhoc = input("nganh hoc co do dai khong qua 40\nMoi nhap lai: ")	
		else:
			break
	while(DTB):	
		if(DTB <= 0 or DTB > 10):
			DTB = float(input("ĐTB > 0 and < 10,\nMoi nhap lai: "))
		else:
			break
	sinhvien = student(hoten,namsinh,quequan,nghenghiep,MSSV,nganhhoc,DTB)
	dsSV.append(sinhvien)

n = int(input("Nhap so luong sv: n = "))
for i in range(n):
	print("Nhap sinh vien thu %d: "%(i+1))
	nhapSV()

for i in dsSV:
	print("---------------------------------------------------------------------------------------------------------")
	print("\t\tSinh vien ",dsSV.index(i)+1)
	print("---------------------------------------------------------------------------------------------------------")
	print("Ho ten : ",i.hoten)
	print("Nam sinh :",i.namsinh)
	print("Que quan :",i.quequan)
	print("MSSV :",i.MSSV)
	print("Nganh Hoc :",i.nganhhoc)
	("Diem trung binh :",i.DTB)
	print("Xep Loai :",i.rank())

#Cau 7
class Exchange:
	def __init__(self,Serial, Date,Amount, ExchangeType):
		self.Serial = Serial
		self.Date = Date
		self.Amount = Amount
		self.ExchangeType = ExchangeType

	def PrintExchange(self):
		return "Chua co chuc nang !"
	CashUp(self):
		return "Chua co chuc nang !"

#Cau 8
class Exchange:
	def __init__(self,Serial, Date,Amount, ExchangeType):
		self.Serial = Serial
		self.Date = Date
		self.Amount = Amount
		self.ExchangeType = ExchangeType

	def PrintExchange(self):
		return ""
	CashUp(self):
		return ""

class GoldExchange(Exchange):
	def __init__(self,Serial,Date,Amount,ExchangeType,GoldType,UnitPrice):
		super().__init__(Serial,Date,Amount,ExchangeType)
		self.GoldType = GoldType
		self.UnitPrice = UnitPrice
	def CashUp(self):
		kq = self.Amount*self.UnitPrice
		return "Cash up "
	def PrintExchange(self):
		print("Thong tin giao dich vu dinh dang: ")
		return "Serial – Date – GoldType – UnitPrice – Amount – Cash Up = ".format(self.Serial,self.Date,self.GoldType,self.UnitPrice,self.Amount,self.CashUp())