'''
Question's too long
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y1 = 3*x - 4
y2 = x**2 + 2*x - 15
y3 = 5*(x-1)*(x-2)*(x-3)
y4 = np.exp(x)
y5 = np.log(x)
y6 = np.sin(x)

plt.plot(x, y1)
plt.title('f(x)=3x−4')
plt.show()

plt.plot(x, y2)
plt.title('f(x)=x^2 +2x−15')
plt.show()

plt.plot(x, y3)
plt.title('f(x)=5(x−1)(x−2)(x−3)')
plt.show()

plt.plot(x, y4)
plt.title('f(x)=e^x')
plt.show()

plt.plot(x, y5)
plt.title('f(x)=logx')
plt.show()

plt.plot(x, y6)
plt.title('f(x)=sinx')
plt.show()
