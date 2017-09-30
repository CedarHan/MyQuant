import numpy as np
import numpy.linalg as nlg

# a = np.arange(100)
# print(a)
# a = a.reshape(2, 5, 5, 2)
# print(a)
# print(a.shape, a.ndim, a.size)
#
# raw = [1, 2, 3, 4]
# a = np.array(raw)
# print(a)
#
# raw = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
# b = np.array(raw)
# print(b)
#
# d=(4,5)
# d=np.zeros(d)
# print(d)
# d=(2,2,2)
# d=np.ones(d,dtype=int)
# print(d)
# c = np.random.rand(4)
# print(c)
# a = np.array([[1.0, 2], [2, 4]])
# print("a:")
# print(a)
# b = np.array([[3.2, 1.5], [2.5, 4]])
# print("b:")
# print(b)
# print("a+b:")
# print(a + b)
# print(3 * a)
# print(2 + b)
# a /= 2
# print(a)
# print(np.exp(a))
# print(np.sqrt(a))
# print(np.square(a))
# print(np.power(a, 3))
# a = np.arange(20).reshape(4, 5)
# print('a:\n', a)
# print('sum(a):', str(a.sum()))
# print('max(a):', str(a.max()))
# print('min(a):', str(a.min()))
# print('max value of each row:', str(a.max(axis=1)))
# print('min value of each column:', str(a.min(axis=0)))
# print('min value of each column:', str(a.min(axis=0)))
# a = np.arange(20).reshape(4, 5)
# a = np.asmatrix(a)
# print(type(a))
#
# b=np.matrix('1,2;3,4')
# print(b)
# print(type(b))
#
# c=np.arange(2,45,3).reshape(5,3)
# print(c)
# c=np.mat(c)
# print(c)
#
# d=np.linspace(0,1,9)
# print(len(d))
# print(d)

# a = np.arange(20).reshape(4, 5)
# print(a[2][1])
# a = np.asmatrix(a)
# b=np.arange(2,45,3).reshape(5,3)
# print(a)
# print(b)
# print(a*b)
# print(a[:,[1,3,4]])
# print(a[:,0]>5)
# print(a[:,2][a[:,0]>=5])
# loc=np.where(a==11)
# print(loc)
# print(a[loc[0][0],loc[1][0]])
# print(a[2,1])
# print(a[0][1]) matrix can not get value like this
# a=np.random.rand(2,4)
# print(a)
# a=np.transpose(a)
# print(a)
# b=np.random.rand(2,4)
# b=np.mat(b)
# print(b)
# print(b.T)

# a=np.random.rand(3,3)
# a=np.mat(a)
# print(a)
# ia=nlg.inv(a)
# print(ia)
# print(a*ia)
#
# a=[[1,2],[3,4]]
# b=[[-2,1],[1.5,-0.5]]
# a=np.mat(a)
# print(a)
# ia=nlg.inv(a)
# print(ia)
# print(a*ia)
# print(a*b)

# a=np.random.rand(3,3)
# print(a)
# [eig_value, eig_vector] =nlg.eig(a)
# print(eig_value,'\n',eig_vector)
# print((a*eig_value))
# print()
# print((eig_vector*eig_value))
# print(a*eig_vector)

# a=[[1,2],[1,2]]
# b=[[1,2],[1,2]]
# print(a==b)

a=np.array((1,2,3))
b=np.array((4,5,6))
c=np.column_stack((a,b))
print(c)

a=np.random.rand(2,2)
b=np.random.rand(2,2)
print(a,'\n',b)
print(np.hstack([a,b]))
print(np.vstack([a,b]))

a[0,1]=np.nan
print(np.isnan(a))
print(a==np.nan_to_num(a))
















