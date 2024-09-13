import numpy as np
from numpy import cos, pi, sin, exp
import matplotlib.pyplot as plt

N = 10
n = np.arange(N)
x = cos(2*pi/5*n)

m_array = np.arange(-5, 6, 1)
Xm = np.zeros(len(m_array))

for m in m_array:
    Xm[m] = np.sum(x*np.e**(-2j*pi*m*n/N))


plt.stem(m_array, np.abs(Xm))
