import numpy as np
A_list = list(map(int,input().split(" ")))
B_list = list(map(int,input().split(" ")))

A = np.array(A_list)
B = np.array(B_list)

A_B_inner = np.inner(A,B)
A_B_outer= np.outer(A,B)

print(A_B_inner)
print(A_B_outer)