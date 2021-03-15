# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:18:35 2021

@author: scil
"""


import numpy as np
import matplotlib.pyplot as plt
time = np.arange(0, 10, 0.1)
amplitude = np.cos(time)

plt.plot(time,amplitude)
plt.title("Cosine curve")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()