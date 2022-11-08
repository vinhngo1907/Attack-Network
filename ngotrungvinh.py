#Họ tên: Ngô Trung Vinh
#MSSV: B1709321

Câu 1:
print("Hello! Welcome tp Python!")

Câu 2:
s = input("Moi nhap ho ten: ")
print("Hello "+s+", Welcome to Python")

Câu 3:
a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
while b == 0:
	b = int(input("NHap lai b = "))
	if b != 0:
		break
if b != 0:
	print("%d + %d = %d"%(a,b,a+b))
	print("%d - %d = %d"%(a,b,a-b))
	print("%d * %d = %d"%(a,b,a*b))
	print("%d / %d = %d"%(a,b,int(a/b)))
	print("a % b = ",a%b)
	print("%d ** %d = %d"%(a,b,a**b))
	
Câu 4:
import math
r = int(input("Nhap ban kinh: "))
C = 2*r*math.pi
print("Chu vi hinh tron: %f"%C)
S = r**2*math.pi
print("Dien tich hinh tron: %f"%S)

Câu 5:
def giaiThua(n):
	if n == 1:
		return 1
	else:
		return n*giaiThua(n-1)
tl = 'y'
while tl == 'y':
	n = int(input("Nhap so nguyen: n = "))
	if n < 0:
		n = int(input("Nhap lai n = "))
	else:		
		print("%d! = %d"%(n,giaiThua(n)))
		tl = input("Ban muon tiep tuc khong?(y/n): ")
		if tl == 'n':
			break

Câu 6:
import math
a = int(input("a = ")); b = int(input("b = ")); c = int(input("c = "))
if a == 0:
	if b == 0:
		if c == 0:
			print("Phuong trinh vo so nghiem !")
		else:
			print("Phuong trinh vo nghiem !")
	else:
		if c == 0:
			print("Phuong trinh co 1 nghiem x = 0")
		else:
			print("Phuong trinh co nghiem: x = ",float(-c/b))
else:
	delta = b**2 - 4*a*c
	if delta < 0:
		print("Phuong trinh vo nghiem !")
	elif delta == 0:
		print("Phuong trinh co nghiem kep: ",float(-b/2*a))	
	else:
		print("Phuong trin co 2 nghiem: ")
		print("x1 = ",float((-b-math.sqrt(delta))/(2*a)))
		print("x1 = ",float((-b+math.sqrt(delta))/(2*a)))
			
Câu 7:
list = []
for i in range(5000,7001):
	if i % 7 == 0 and i % 5 !=0:
		list.append(i)
		print(i)

print("\t\t\tDanh sach cac so can tim\n",list)

Câu 8:
x = int(input("Nhap x = "))
s =''
while x > 0:
	i = x%2
	s = str(i)+s
	x = int(x/2)
print("Change binary: %s"%s)

Câu 9:
a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
c = a; d = b;
while b != 0:
	if a > b:
		a = a -b
	else:
		b = b -a
		
i = (c*d)/a
print("UCLN(%d,%d) = %d"%(c,d,a))
print("BCNN(%d, %d) = %d"%(c,d,i))

Câu 10:
n = int(input("Nhap n = "))
def checkSNT(x):
	if x < 2:
		return False
	for i in range(2,int(x/2)+1):
		if(x%i == 0):
			return False
	return True
'''	
if(checkSNT(x)):
	print("La so nguyen to !")
else:
	print("Khong la so nguyen to!")
'''
list = []
for i in range(n+1):
	if(checkSNT(i)):
		list.append(i)
		print(i)
	else:
		pass
print("Danh sach cac so nt nho hon n: ",list)		

Câu 11:
def checkSNT(x):
	if x < 2:
		return False
	for i in range(2,int(x/2)+1):
		if(x%i == 0):
			return False
	return True

list = []	
print("Liet ke tat ca cac so co 4 chu so:");
#for (i = 10001; i < 99999; i+=2):
'''
for i in range(1000, 9999):   
	if (checkSNT(i)):
		list.append(i)
		#print("%d\n"%i)
	else:
		pass
'''
i = 1001
while i >= 1001 and i <= 9999:
	if(checkSNT(i)):
		list.append(i)
	i+=1	
print("\t\t\tDanh sach cac so nguyen to 4 chu so\n",list)	

Câu 12:
n = int(input("Nhap n = "))
#list = []
tong = 0
temp = n
while n > 0:
	if n <= 0:
		n = int(input("Nhap n = "))
	else:
		m = n %10
		tong = tong + m
		n = int(n/10)
		
print("Tong cac chu so trong %d = %d"%(temp,tong))

Câu 13:
list = []
for i in range(1000,2001):
	if(i % 2!=0):
		list.append(i)
		print(i)
	else:
		pass

print("Danh sach cac so le: ",list)

Câu 14:
n = int(input("Nhap n = "))
while n < 0:
	if(n >= 0):
		break
s = 0
for i in range(n):
	s= s + (i/(i+1))
print("Total: ",s)	

Câu 15:
def dayFibonacci(n):
    f0 = 0;
    f1 = 1;
    fn = 1;
 
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        for i in range(2, n):
            f0 = f1;
            f1 = fn;
            fn = f0 + f1;
        return fn;
		
s = "";
n = int(input("Enter a number: "))

for i in range(n):
    s = s + str(dayFibonacci(i)) + ", ";

print(s)