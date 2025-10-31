import numpy as np
nr=int(input("enter the number of rows"))
nc=int(input("enter the number of coloums"))
print('enter the entries in a single line seperated by spaces:')
entries=list(map(int,input().split()))
matrix=np.array(entries).reshape(nr,nc)
print("matrix x is a follows;",'\n',matrix)
print("transpose of matrix x is as follows",'\n',np.transpose(matrix))

