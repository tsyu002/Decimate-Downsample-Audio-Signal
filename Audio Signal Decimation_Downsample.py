import numpy as np
import random

###DECIMATION
def decimate_by_2(conv):
    dec=conv[::2]
    return dec

###LOW PASS FILTERING
def downsample_by_2(inp, filt):
    ##Reference: https://docs.scipy.org/doc/numpy/reference/generated/numpy.convolve.html
    conv=np.convolve(inp, filt, mode='same')
    down_sampled=decimate_by_2(conv)
    return down_sampled

###TEST CASE
##Create random input signal. 2 options are given below.
inp = [random.randrange(1, 1000, 1) for i in range(32)]
#inp = list(range(0,32))

##Using given Kaiser Smoothing Filter for filt
filt = [-0.01452123, -0.0155227 ,  0.01667252,  0.01800633, -0.01957209, -0.0214361 ,  0.02369253,  0.02647989, -0.03001054, -0.03462755, 0.04092347,  0.05001757, -0.06430831, -0.09003163,  0.15005272, 0.45015816,  0.45015816,  0.15005272, -0.09003163, -0.06430831, 0.05001757,  0.04092347, -0.03462755, -0.03001054,  0.02647989, 0.02369253, -0.0214361 , -0.01957209,  0.01800633,  0.01667252, -0.0155227 , -0.01452123]
output = downsample_by_2(inp,filt)

##Print Results
print(f'The Output Array is: {output}')
print(f'Output returns a {type(output)}')
print(f'Length of Array is {len(output)}')
