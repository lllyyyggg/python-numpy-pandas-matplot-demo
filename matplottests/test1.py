import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 10, 6)
y = 2 * x + 1

fig = plt.figure()
plt.xlim(0, 10)
plt.ylim(0, 20)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
new_x_ticks = np.linspace(0, 10, 11)
plt.xticks(new_x_ticks)
# plt.yticks([2.5, 7.5, 12.5, 17.5], [r'$too\ bad$', r'$bad$', r'$nice$', r'$really\ good$'])


ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

x_temp = 3
y_temp = 2 * x_temp + 1
plt.scatter([x_temp, 0, 1, 2, 3, 4, 5, 6], [y_temp, 0, 4, 5, 8, 11, 10, 12], s=60, color='#ff00ff')
plt.plot([x_temp, x_temp], [y_temp, 0], color='#cccccc', linewidth=2.5, linestyle='--')
plt.annotate(r'$2x+1=%s$' % y_temp, xy=(x_temp, y_temp),
             xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
l1, = plt.plot(x, y, color='#0086ff', linewidth=1.0, linestyle='--')
plt.legend(loc='best', handles=[l1], labels=[r'$y=2x+1$'])
plt.text(0.5, 12.5, r'$this\ is\ some\ text\ \alpha$', fontdict={'size': 16, 'color': 'red'})
plt.show()
