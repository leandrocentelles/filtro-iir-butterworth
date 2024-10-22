#IMPLEMENTACIÓN DE UN FILTRO IIR - BUTTERWORTH

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def matriz_TFD(N, Nfft):
    k = np.arange(Nfft)
    if N is None: N = Nfft
    n = np.arange(N)
    U = np.matrix(np.exp(1j * 2*np.pi/Nfft * k * n[:, None]))
    return U/np.sqrt(Nfft)

# Creamos una señal que consta de la suma de dos senoidales y la graficamos.
frecuencia_de_muestreo = 5000.0
frecuencia_de_corte_del_filtro = 1300.0
T = 0.05
numero_de_muestras = T * frecuencia_de_muestreo #número de muestras
t = np.linspace(0, T, int(numero_de_muestras), endpoint=False)
print("Frecuencia de muestreo: ", frecuencia_de_muestreo)
print("Frecuencia de corte: ", frecuencia_de_corte_del_filtro)

#senal = (10*np.sin(2000*t*2*np.pi) + 10*np.sin(400*t*2*np.pi))
senal = (10*np.sin(2000*t*2*np.pi) + 10*np.sin(400*t*2*np.pi) + 10*np.sin(1700*t*2*np.pi) + 10*np.sin(900*t*2*np.pi))

plt.figure(1)
plt.clf()
plt.title("Señal original")
plt.ylabel("Amplitud")
plt.xlabel("Tiempo")
plt.plot(t, senal)

# Se crea un filtro con una frecuencia de corte igual a frecuencia_de_corte_del_filtro.
nyquist = 0.5 * frecuencia_de_muestreo #frecuencia de Nyquist
frec_corte_normalizada = frecuencia_de_corte_del_filtro / nyquist
orden_del_filtro = 6
#tipo_de_filtro = 'lowpass'
tipo_de_filtro = 'highpass'

#Butterworth
Butterworth = signal.butter(orden_del_filtro, frec_corte_normalizada, btype=tipo_de_filtro, output='sos')

senal_filtrada = signal.sosfilt(Butterworth, senal)

plt.figure(2)
plt.clf()
plt.title("Señal filtrada")
plt.ylabel("Amplitud")
plt.xlabel("Tiempo")
plt.plot(t, senal_filtrada)

"""
Para calcular la transformada de Fourier de la señal x[n], se usa la expresión X=U.H*x, donde U.H es el complejo
conjugado de la matriz U. Abajo se calcula la transformada de Fourier de la señal creada.
"""

U = matriz_TFD(N=len(senal), Nfft=frecuencia_de_muestreo)
#print(U.shape)
senal.shape = (len(senal), 1) #Se convierte en vector columna para poder multiplicar con la matriz.
TF_senal_original = U.H*senal # TF_senal_original es la transformada de Fourier de senal
valores_TFD_senal_original = np.abs(TF_senal_original)

#Se calcula la transformada de Fourier de la señal filtrada.
U_filtrada = matriz_TFD(N=len(senal_filtrada), Nfft=frecuencia_de_muestreo)
#print(U_filtrada.shape)
senal_filtrada.shape = (len(senal_filtrada), 1) #Se convierte en vector columna para poder multiplicar con la matriz.
TF_senal_filtrada = U_filtrada.H*senal_filtrada # TF_senal_filtrada es la transformada de Fourier de senal_filtrada
valores_TFD_senal_filtrada = np.abs(TF_senal_filtrada)

plt.figure(3)
plt.plot(valores_TFD_senal_original)
plt.title("Frecuencias de la señal original")
plt.ylabel("Potencia")
plt.xlabel("Frecuencia [Hz]")
plt.xlim(0,2500)

plt.figure(4)
plt.plot(valores_TFD_senal_filtrada)
plt.title("Frecuencias de la señal filtrada")
plt.ylabel("Potencia")
plt.xlabel("Frecuencia [Hz]")
plt.xlim(0,2500)

plt.show()
