from matrix import *

li1 = [[1,2],[2,1]]
m1 = matrix.from_list(li1)

m2 = matrix.eye(2)
m3 = matrix.from_list([[1,0],[0,1]])
print(m3 == m2)
#print(m1 * m2)
print(matrix.get_inverse(m1))
print(1 in m1)
