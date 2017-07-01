import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 基本使用
'''
x = np.linspace(-2, 2, 100)
y1 = np.cos(np.pi * x)
y2 = np.sin(np.pi * x)

plt.plot(x, y1, 'go', label=r"$y1=\cos(\pi \times x)$", alpha=0.8, linewidth=0.7)
plt.plot(x, y2, 'r-', label=r"$y2=\sin(\pi \times x)$", alpha=0.8, linewidth=0.7)

plt.annotate("Important Point", (0, 1), xytext=(-1.5, 1.1),
             arrowprops=dict(arrowstyle='->'))

plt.xlabel('x-axis')
plt.ylabel('y-axis')

# 设置座标范围[xmin, xmax, ymin, ymax]
plt.axis([-2.1, 2.1, -1.2, 1.2])

# 显示标签
plt.legend()
# 显示网格
plt.grid(alpha=0.4)

plt.title("Two plots", color=(0.1, 0.3, 0.5))
plt.show()

'''

# 进阶使用
'''
# 绘制子图[subplot]
plt.style.use('ggplot')  # 设置绘图风格
x = np.linspace(-2, 2, 100)
y1 = np.sin(np.pi * x)
y2 = np.cos(np.pi * x)
y3 = np.tan(np.pi * x)
y4 = x

plt.subplot(221)
plt.plot(x, y1)

plt.subplot(222)
plt.plot(x, y2)

plt.subplot(223)
plt.plot(x, y3)

plt.subplot(224)
plt.plot(x, y4)

plt.show()
'''
