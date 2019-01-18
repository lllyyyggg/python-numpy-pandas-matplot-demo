import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# 复杂的图
plt.figure()
# method 1
# ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
# ax1.plot([1, 2], [1, 2])
# ax1.set_title('one')
#
# ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2,)
# ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2,)
# ax4 = plt.subplot2grid((3, 3), (2, 0))
# ax5 = plt.subplot2grid((3, 3), (2, 1))


# method 2
# gs = gridspec.GridSpec(3, 3)
# ax1 = plt.subplot(gs[0, :])
# ax2 = plt.subplot(gs[1, :2])
# ax3 = plt.subplot(gs[1:, 2])
# ax4 = plt.subplot(gs[-1, 0])
# ax5 = plt.subplot(gs[-1, -2])


# method 3
# fig, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)
# ax11.scatter([1, 2], [1, 2])
plt.show()
