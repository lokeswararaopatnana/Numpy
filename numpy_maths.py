import numpy as np
# a=np.array([[12,13,14],
#            [7,8,9]])
# b=np.array([[3,2,1],
#            [3,2,1]])
# c=a+b
# d=a-b
# e=a*b
# f=a/b
# g=4*a
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)

# a=np.eye(2)   # here eye is euals to identity matrix or unit matrix
# print(a)
# b=np.eye(3,dtype=int)
# print(b)

# k=np.array([x for x in range(9)])
# j=k.reshape(3,3)
# print(j)

# h=np.array([[5.2,3.4,8.6],
#            [4.1,5.8,9.7]])
# m=h.astype('int')  # here float is converted into int
# print(m)

# n=np.array([[1,0,0],
#             [1,1,1],
#             [1,0,1]])
# d=n.astype('bool')
# print(d)

# o=np.array([[3,5,8],
#             [4,8,3]])
# p=np.array([[9,8,6],
#             [7,2,3]])
# f=np.hstack((o,p))
# print(f)

# q=np.array([[5,4,9],
#            [4,7,2],
#            [1,8,3],
#            [7,5,3]])
# r=np.array([[1,5,9],
#             [4,2,6],
#             [3,2,9],
#             [7,4,6]])
# s=np.vstack((q,r))
# print(s)

# t=[x for x in range(0,51,1)]
# u=np.array(t)
# print(u)

# v=np.arange(0,51,1)
# print(v)

# w=np.array([1,2,3,4,5,6])
# x=np.array([1,2,6,4,3,6])
# print(np.where(w==x))

# z=np.full((3,3),6)
# print(z)

# a=np.array([[1,2,3],
#             [4,5,6],
#             [7,8,9]])
# b=np.array([[2,3,4],
#             [5,6,7],
#             [8,9,10]])
# c=a@b
# print(c)
# d=np.matmul(a,b)
# print(d)

# e=np.array([[1,2,3],
#             [4,5,6],
#             [8,5,2]])
# f=e.T   # T is called as Transpose
# print(f)

print(dir(np))