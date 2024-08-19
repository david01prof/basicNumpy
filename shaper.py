import numpy as np

# create 1-D Numpy Array and get Shape
np1 =np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np1)
print(np1.shape)

# create 2-D Array and get Shape, (rows/columns-elements)
#np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
#print(np2)
#print(np2.shape)

# reshape 2-D
np3 = np1.reshape(3,4)
print(np3)

# reshape 3-D
np4 = np1.reshape(2,3,2)
print(np4)

# flatten to 1-D
np5 = np4.reshape(-1)
print(np5)