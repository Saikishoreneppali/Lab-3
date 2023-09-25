import numpy as np

v1 = np.array([1, 2, 3, 4, 5, 6])
print(v1)

v2 = np.array([7, 8, 9, 10, 11, 12])
print(v2)

print(v1 + v2)

print (v1 * v2)

print(v1.shape) # it shows that v1 is 6 times nothing matrix 
# if we want to make it a 6 by 1 vector:
v1 = np.array([[1], [2], [3], [4], [5], [6]])
print(v1.shape)

v2 = np.array([[7], [8], [9], [10], [11], [12]])
print(v2.shape)

# in order to do matrix multiplication, we should multiply one by the transpose of the other 

print(np.matmul(v1,v2.T))
print("or")
print(np.matmul(v1,np.transpose(v2))) 
print(v2.T.shape) 

# @ also means matrix multiplication 
print(v1.T @ v2) # which is a 1 by 1 vector or just a number

x = np.array([[[0], [1], [2], [1], [9], [9]],[[2], [2], [1], [0], [0], [0]]])    #2 by 6 matrix
print(x.shape)