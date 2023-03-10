import numpy as np

'''a1 = np.zeros((3, 3))
a2 = np.ones((3, 2))

n1 = np.arange(10, 151, 10)
n1_shape = n1.reshape(3, 5)

a3 = np.hstack([a1, a2])
n1_shape_one = np.vstack([a3, n1_shape])
final = np.tile(n1_shape_one, (2, 1))
print(final)'''

'''zero = np.zeros((3, 3))
one = np.ones((3, 2))

hop = np.reshape(np.arange(10, 151, 10), (3, 5))
res = np.tile(np.vstack([np.hstack([zero, one]), hop]), (2, 1))
print(res)'''
'''
a = np.zeros((3,3))
b = np.ones((3,2))
c = np.hstack([a,b])
d = np.arange(10,51,10)
e = d+50
f = e+50

print(np.tile(np.vstack([c,d,e,f]),(2,1)))
'''