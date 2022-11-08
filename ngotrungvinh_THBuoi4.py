#Ngô Trung Vinh
#MSSV:B1709321
import numpy as np
import matplotlib.pyplot as plt
import pylab as p 
#Câu 1
arr1 = np.array([1, 3, 5, 7, 9])
print("Câu 1: ",arr1)
#Câu 2
arr2 = np.array([(1, 3, 5, 7, 9),(2, 4, 6, 8 ,10)])
print("Câu 2: ",arr2)
#Câu 3
arr3 = np.zeros(10,dtype = int)
# print("Câu 3: ",arr3)
arr3[6] = 13
print("Câu 3: ",arr3)
#Câu 4
arr4 = np.ones((5,5),dtype = int)
for x in range(1,4):
	arr4[1,x] = 0
	arr4[2,x] =0
	arr4[3,x] = 0
print("Câu 4: \n",arr4)
#Câu 5
arr5 = np.ones((3,3),dtype = int)
r = np.pad(arr5, (1, 1), 'constant', constant_values=(0))
print("Câu 5:\n ",r)

#Câu 6
r1 = np.array([10, 20, 40, 60,70] )
r2 = np.array([10, 30, 50, 60])
r3 = np.intersect1d(r1,r2)
print("Câu 6: ",r3)
#Câu 7
arr7 = np.linspace(1,100,retstep=False,num = 100,dtype = int)
l7 =[]
for i in arr7:
	if i % 2 == 0:
		l7.append(i)
	else:
		pass
print("Câu 7:\n A = ",l7)

#Cau 8 
print("\t\t---------Câu 8---------\t\t")
x =  np.linspace(-10,10,num = 1000)
# print(x)
y = np.sin(x)
plt.scatter(x, y)
plt.show()

#Câu 9
print("\t\t---------Câu 9---------\t\t")
x =  np.linspace(-5,5,num = 1000)
# print(x)
y = x**3-2*(x**2)+x+5
plt.scatter(x, y)
plt.show()

#Câu 10
print("\t\t---------Câu 10---------\t\t")
x =  np.linspace(-10,10,num = 1000)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,x,z)
plt.xlabel('x values from -10 to 10')  # string must be enclosed with quotes '  '
plt.ylabel('sin(x) and cos(x)')
plt.title('Đồ thị hình sin và cos')
plt.legend(['sin(x)', 'cos(x)'])      # legend entries as seperate strings in a list
plt.show()

#Câu 11
print("\t\t---------Câu 11---------\t\t")
from mpl_toolkits.axes_grid.inset_locator import inset_axes

x = np.arange(-10, 10, 0.01)
sinx = np.sin(x)
tanx = np.tan(x)

fig, ax = plt.subplots( 1, 2, sharey='row', figsize=(9, 3) )

for i, f in enumerate([sinx, tanx]):
    ax[i].plot( x, f, color='red' )
    ax[i].set_ylim([-2, 2])

    # create an inset axe in the current axe:
    inset_ax = inset_axes(ax[i],
                          height="30%", # set height
                          width="30%", # and width
                          loc=10) # center, you can check the different codes in plt.legend?
    inset_ax.plot(x, f, color='green')
    inset_ax.set_xlim([0, 5])
    inset_ax.set_ylim([0.75, 1.25])
plt.show()