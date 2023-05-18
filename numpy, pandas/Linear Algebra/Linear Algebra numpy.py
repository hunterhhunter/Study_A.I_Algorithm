import numpy as np

A = np.array([[1,2], [3, 4]])
print(A)
print(A*4)
print(3**A)
print(A*A)
print()
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

print(np.dot(x, y))
print(x*y)
print()

print(x==y)
print(y>x)

a = np.array([1,1,0,0], dtype=bool)
b = np.array([0,1,1,0], dtype=bool)

print(np.logical_or(a,b), np.logical_and(a,b),
np.logical_xor(a,b),
np.logical_not(b))

c = np.array([1, 2,3,4,5])
print()
print(np.sum(c))
print(c.sum())

print(c.min())
print(c.max())

print(c.argmax()) #최댓값 인덱스 반환
print(c.argmin()) #최솟값 인덱스 반환

d = np.array([True, True, False])
e = np.array([True, True, True])

np.all(d) #모든값이 T인가
np.all(e)

np.any(d) #하나라도 T인가
np.any(e)

np.mean(array) #평균값
np.median(array) #중간값
np.std(array) #표준편차