# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 13:58:19 2022

@author: macwr
"""

import numpy as np
import matplotlib.pyplot as plt


#computes wiener process
def wiener_process(dt = 0.1, x0 = 0, n=1000):
    
    #create data array of all zeros
    W = np.zeros(n+1)
    
    #create timestamps of appropriate size
    t = np.linspace(x0, n, n+1)
    
    #cumulative random walk data
    W[1: n+1] = np.cumsum(np.random.normal(0, np.sqrt(dt),n))
    return t, W

def plot_process(t, W):
    plt.plot(t, W)
    plt.xlabel('Time(t)')
    plt.ylabel('Wiener-Process W(t)')
    plt.title('Wiener-Process')
    plt.show
    
if __name__ == '__main__':
        time, data = wiener_process()
        plot_process(time, data)
        