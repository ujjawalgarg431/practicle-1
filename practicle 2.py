import numpy as np
nr=int(input("enter the number of rows"))
nc=int(input("enter the number of coloums"))
print('enter the entries in a single line seperated by spaces:')
entries=list(map(int,input().split()))
matrix=np.array(entries).reshape(nr,nc)
print("matrix x is a follows;",'\n',matrix)
print("the rank of a matrix is:",np.linalg.matrix_rank(matrix))