# coding:utf-8

import numpy as np 
import matplotlib.pyplot as plt
from numpy import random as nr

# 画坐标方法
def draw_point(x, y):
	fig = plt.figure()
	axes = plt.gca()
	axes.set_xlim([0,10])
	axes.set_ylim([0,10])
	for i in range(len(y)):
		if y[i] == 1:
			plt.plot(x[i][0], x[i][1], 'ro')
		else:
			plt.plot(x[i][0], x[i][1], 'bo')
	# plt.show()

input_x = np.array([[1, 3], [2, 6], 
					[4, 2], [5, 3], 
					[2, 8], [7, 2],
					[3, 6], [9, 5],
					[5, 5], [5, 8]])
input_y = np.array([-1, -1, 1, 1, -1, 
					1, -1, 1, -1, -1])

fig = draw_point(input_x, input_y)

w = [0, 0]
b = 10
lr = 1

for i in range(100):
	wrong_count = 0
	for j in range(len(input_y)):
		if input_y[j] != np.sign(np.dot(w, input_x[j]) + b):
			w += lr * input_y[j] * input_x[j]
			b += lr * input_y[j]
			wrong_count += 1
	if wrong_count == 0:
		break

print w 
print b

# 两点画直线
def draw_line(w, b):
	line_x = [0, 10]
	line_y = [0, 0]
	for i in range(len(line_x)):
		line_y[i] = (-w[0] * line_x[i] -b) / (w[1] + 1e-6)
	plt.plot(line_x, line_y)
draw_line(w, b)	
plt.show()


