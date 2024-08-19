import numpy as np

# np.sort() NUMERICAL
np1 = np.array([6,7,4,9,0,2,1])

print(np1)
print(np.sort(np1))

# Alphabetical

np2 = np.array(["John","Tina","Aaron","Zed"])

print(np2)
print(np.sort(np2))

# Booleans T/F

np3 = np.array([True,False,False,True])

print(np3)
print(np.sort(np3))

# return a copy not change the original

print(np1)
print(np.sort(np1))
print(np1)

# 2-d

np4 = np.array([[1,3,4,8],[2,5,6,3]])
print(np.sort(np4))