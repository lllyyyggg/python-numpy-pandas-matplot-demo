import matplotlib.pyplot as plt
import numpy as np

# 数据
x = np.linspace(-2, 10, 6)
y = 2 * x + 1

# 创建figure
fig = plt.figure()
# 限制x轴的范围
plt.xlim(0, 10)
# 限制y轴的范围
plt.ylim(0, 20)

# 给x和y打上label
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

# 给x轴重新设置坐标分布
new_x_ticks = np.linspace(0, 10, 11)
plt.xticks(new_x_ticks)
# plt.yticks([2.5, 7.5, 12.5, 17.5], [r'$too\ bad$', r'$bad$', r'$nice$', r'$really\ good$'])

# 或者骨架Get Current Axis
ax = plt.gca()
# 设置右边和上面的颜色为肉眼不可见
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 设置x轴为bottom轴，设置y轴为left轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 设置x和y轴的相对偏移量
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 描一个点
x_temp = 3
y_temp = 2 * x_temp + 1
# 将点scatter到坐标上
plt.scatter([x_temp, 0, 1, 2, 3, 4, 5, 6], [y_temp, 0, 4, 5, 8, 11, 10, 12], s=60, color='#ff00ff')
# 过点做x轴的垂线
plt.plot([x_temp, x_temp], [y_temp, 0], color='#cccccc', linewidth=2.5, linestyle='--')
# 给点设置annotation, 注解
plt.annotate(r'$2x+1=%s$' % y_temp, xy=(x_temp, y_temp),
             xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
# line 1
l1, = plt.plot(x, y, color='#0086ff', linewidth=1.0, linestyle='--')

# 设置legend, 也就是那些对线条进行说明的小块
plt.legend(loc='best', handles=[l1], labels=[r'$y=2x+1$'])
# 给整个图设置文本说明
plt.text(0.5, 12.5, r'$this\ is\ some\ text\ \alpha$', fontdict={'size': 16, 'color': 'red'})

# 展示
plt.show()
