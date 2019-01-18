import matplotlib.pyplot as plt
import numpy as np
# 加上标注
x = np.linspace(-1, 1, 50)
y = 2 * x + 1
y2 = x ** 2

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
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='down')
plt.legend(loc='best', handles=[l1, l2], labels=['aaa', 'bbb'])
plt.show()
