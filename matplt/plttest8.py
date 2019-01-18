import matplotlib.pyplot as plt
import numpy as np
# 2D图像
a = np.array([0.33, 0.24, 0.42, 0.57]).reshape((2, 2))

plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')
plt.colorbar(shrink=0.9)


plt.xticks(())
plt.yticks(())
plt.show()
