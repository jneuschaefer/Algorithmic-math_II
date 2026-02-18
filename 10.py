import numpy as np
import matplotlib.pyplot as plt

#Aufgabenteil a)
def fft(f):
    if len(f) == 1:
        return f
    else:
        g = fft(f[::2])
        u = fft(f[1::2])
        c = np.array([None]*len(f))
        for k in range(int(len(f)/2)):
            c[k] = g[k] + u[k]*np.exp(-2j*np.pi*k/len(f))
            c[k+int(len(f)/2)] = g[k] - u[k]*np.exp(-2j*np.pi*k/len(f))
        return c

def ifft(coeffs):
    if (n := coeffs.shape[0]) & (n-1) != 0:
        return

    return np.conj(fft(np.conj(coeffs))) / n

#Aufgabenteil c)
t = np.arange(-np.pi, np.pi, np.pi/8)
print("Numpy:")
print(np.fft.ifft(np.fft.fft(np.sin(t))))
print("eigene fft")
print(np.fft.ifft(fft(np.sin(t))))
print("eigene ifft")
print(ifft(np.fft.fft(np.sin(t))))