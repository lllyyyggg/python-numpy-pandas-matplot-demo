import matplotlib.pyplot as plt
import numpy as np

# 加特殊的点的annotation
x = np.linspace(-1, 1, 50)
y = 2 * x + 1

plt.figure()

plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1, 0, 1, 2], [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$excellent$'])

# gca get current axis
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

l1, = plt.plot(x, y, label='up')
plt.legend(loc='best', handles=[l1, ], labels=['aaa', ])

x0 = 0.5
y0 = x0 * 2 + 1
plt.scatter(x0, y0, s=50, color='b')
plt.plot([x0, x0], [y0, 0], 'k--', linewidth=2.5)

# annotation 1
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0),
             xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
# annotation 2
plt.text(-1, 2.5, r'$this\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$', fontdict={'size': 16, 'color': 'r'})
plt.show()
