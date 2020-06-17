import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random


x = 0
y = 100
m = 2
c = 100
x_arr = []
y_arr = []
m_arr = []
c_arr = []
x_dir_arr = []
y_dir_arr = []

obj = 20  #always even 
if obj%2 != 0:
	obj +=1
for i in range(0,obj):
	x_arr.append(random.randint(0,100))
	c_arr.append(random.randint(0,100))
	m_arr.append(random.randint(1,100))
	y_arr.append(0)
	x_dir_arr.append(1)
	y_dir_arr.append(0)

# for i in range(0,int(obj/2)):
# 	m_arr.append(random.randint(1,1000))
# for i in range(0,int(obj/2)):
# 	m_arr.append(random.random())


print (m_arr)

fig,ax = plt.subplots()
ax.set_xlim(0,500)
ax.set_ylim(0,500)
scatter, = ax.plot(x,y, 'ro')

for i in range(len(y_dir_arr)):
	if m_arr[i]>=0:
		y_dir_arr[i] = 1
	else:
		y_dir_arr[i] = 0

speed = 10

def move(x,y,x_dir,y_dir,m,c):

	if x_dir == 1:
		x = x+ (speed/abs(m))
	if x_dir == 0:
		x = x- (speed/abs(m))	
	# if m>1 :
	# 	if x_dir == 1:
	# 		x = x+ (speed/abs(m))
	# 	if x_dir == 0:
	# 		x = x- (speed/abs(m))
	# if m<1 :
	# 	if x_dir == 1:
	# 		x = x+ 1
	# 	if x_dir == 0:
	# 		x = x- 1		


	if x >= 500:
		m = -m
		c = y - m*x		
		x_dir = 0
		

	if x <= 0:
		m = -m
		c = y - m*x		
		x_dir = 1
		

	y  = m*x + c 

	if y >=500 and y_dir == 1: 
		m = -m
		c = y - m*x
		y_dir = 0

	if y <= 0 and y_dir == 0:
		y_dir =1
		m = -m
		c = y - m*x
	
	# print (int(x),int(y),m,y_dir)
	return x,y,x_dir,y_dir,m,c


def animation_frame(i):
	global x_arr,y_arr,m_arr,c_arr,x_dir_arr,y_dir_arr
	for i in range (len(x_arr)):
		x,y,x_dir,y_dir,m,c = x_arr[i],y_arr[i],x_dir_arr[i],y_dir_arr[i],m_arr[i],c_arr[i]
		x_arr[i],y_arr[i],x_dir_arr[i],y_dir_arr[i],m_arr[i],c_arr[i] = move(x,y,x_dir,y_dir,m,c)

	scatter.set_xdata(x_arr)
	scatter.set_ydata(y_arr)
	return scatter



animation = FuncAnimation(fig,func= animation_frame,frames= np.arange(0,10,1), 
						  interval = 1)
plt.show()