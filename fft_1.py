import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft,fftfreq,ifft,fftshift
###################TIME/MOMENTUM DOMAIN########################
p0 = 2
A = np.sqrt(1/(2*p0)) #Amplitude of square wave
t = np.linspace(-p0,p0,1000) 
y = np.zeros_like(t)
y[(t>-p0)*(t<p0)] =A  #ploting over one period


#################Frequency/Position Domain#####################
fft_val = fft(abs((y*t)))
tf = fftfreq(1000,.01)
plt.plot(tf,fft_val)

##############Calculated FFT by Hand########################

x = np.linspace(-p0-p0,p0*2,1000)
y = [((np.sqrt(1/(np.pi*p0)))*np.sin(p0*t))/t for t in x]
plt.plot(x,y)
plt.show()
