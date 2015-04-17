import numpy as np
import matplotlib.pyplot as plt

arr = np.zeros((9,9))

arr[:,:3] = 1
arr[8] = 1


arr[(4,7,1),(5,7,8)] = 1

plt.spy(arr)
plt.show()
