import threading

# def matmult(a,b):
#     zip_b = zip(*b)
#     out = [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
#              for col_b in zip_b] for row_a in a]

#     # for ele_a, ele_b in zip(row_a, col_b)
#     return out

def mult(w,a,i,j, o):
	sum = 0
	for k in range(len(w[0])):

		#print("w:{}, a:{}".format(w[i][k], a[k][j]))
		sum += (w[i][k] * a[k][j])
	o[j][i] = sum
	

def matmult2(w,a):
	#a = w, b = a
	rows_W = len(w)
	cols_W = len(w[0])
	rows_A = len(a)
	cols_A = len(a[0])
	# print("a.r:{}".format(rows_A))
	# print("a.c:{}".format(cols_A))
	# print("w.r:{}".format(rows_W))
	# print("w.c:{}".format(cols_W))
	output = [[0 for row in range(rows_W)]for col in range(cols_A)]
	# print output
	threads = []
	for i in range(rows_W):
		for j in range(cols_A):
			th = threading.Thread(target=mult, args=(w,a,i,j,output))
			th.start()
			threads.append(th)

		for th in threads:
			th.join

	return output







# x = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
# y = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9],[6,7,8,9,10],[7,8,9,10,11],[8,9,10,11,12],[9,10,11,12,13],[10,11,12,13,14]]

# import numpy as np # I want to check my solution with numpy
# from time import time


# mx = np.matrix(x)
# my = np.matrix(y) 
# start = time() 
# z = matmult2(x,y)
# time_par = time() - start
# print('rfunc: {:.2f} seconds taken'.format(time_par))
# print(z)