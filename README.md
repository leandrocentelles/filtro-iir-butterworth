**IMPLEMENTACIÓN DE UN FILTRO BUTTERWORTH EN PYTHON**

La transformada discreta Fourier para la señal x[n] se define de acuerdo con la siguiente ecuación.

![image](https://github.com/user-attachments/assets/ab95fe08-5138-470d-8cd5-b326517536e6)

Donde U representa una matriz de transformación, que se puede definir con la ecuación que se encuentra debajo. 𝑁 es el número de muestras de la señal, y NFFT es el número de puntos de la transformada de Fourier que se desea calcular (debe ser una potencia de 2).

![image](https://github.com/user-attachments/assets/769f736c-394f-45e2-b0df-44f607372644)

El número de puntos de la transformada de Fourier define la resolución en frecuencia, donde cada índice mapea el contenido de frecuencia de la señal en un rango normalizado entre 0 y 2𝜋. Cada índice también mapea la frecuencia de muestreo entre 0 y 𝑓𝑠, por lo tanto, para encontrar la equivalencia entre la frecuencia normalizada, y la frecuencia en Hz, se debe multiplicar la frecuencia normalizada por (𝑓𝑠/2). Luego de definir la matriz, se puede redefinir la transformada de Fourier como una multiplicación de una matriz y un vector (columna).

![image](https://github.com/user-attachments/assets/7220aab3-a5c5-4cec-b3e3-e26e3875ef67)

En términos simples, la TFD toma una señal y calcula cuáles frecuencias están presentes en ella. En términos más técnicos, la TFD transforma la señal del dominio del tiempo al dominio de la frecuencia.

**NumPy**, Numeric Python, es un paquete que dispone de múltiples herramientas para manejar matrices de una forma muy eficiente.

**SciPy** contiene módulos para optimización, álgebra lineal, integración, interpolación, funciones especiales, FFT, procesamiento de señales y de imagen, resolución de ODEs y otras tareas para la ciencia e ingeniería.

**Matplotlib** se utiliza para crear gráficos y diagramas de gran calidad.

Importamos las librerías a utilizar: numpy, scipy y matplotlib.

![image](https://github.com/user-attachments/assets/f3c564fb-c67d-4c06-a411-51c5c8beda95)

La siguiente función construye la matriz U de transformación.

![image](https://github.com/user-attachments/assets/b969beea-525d-4536-af79-54d99dc973fa)

Creamos una señal y determinamos la frecuencia de muestreo y de corte. Luego la graficamos.

![image](https://github.com/user-attachments/assets/7bb361a5-c402-4743-be54-6fac11814c53)

Creamos un filtro IIR, particularmente de tipo Butterworth. Se puede elegir si será pasa bajos o pasa altos. Luego filtramos la señal original, se guarda en la variable señal_filtrada y se grafica.

![image](https://github.com/user-attachments/assets/8c0aa88d-0ac4-487b-af9c-48e70b33a6ff)

Calculamos la Transformada de Fourier Discreta de la señal original y de la señal filtrada, para así pasar del dominio del tiempo al dominio de la frecuencia. Luego graficamos las frecuencias de ambas señales.

La TFD retorna un arreglo de números complejos. Por eso vamos a considerar solo la información de amplitud de la TFD, por ello se hace:
valores_TFD_senal_original = np.abs(TF_senal_original) 
valores_TFD_senal_filtrada = np.abs(TF_senal_filtrada)

![image](https://github.com/user-attachments/assets/5c49f881-8ca7-4371-ba76-10deb260d770)

**EJEMPLO**

Señal original

![Señal original](https://github.com/user-attachments/assets/e49ef98c-8217-4ed5-83e1-8854ac381efe)

Señal filtrada

![Señal filtrada](https://github.com/user-attachments/assets/70d487e1-40b2-4f4d-a422-c0d74b599a80)

Frecuencias de la señal original

![Frecuencias de la señal original](https://github.com/user-attachments/assets/3bd55d70-4cea-4340-bba0-476ddbe7c999)

Frecuencias de la señal filtrada

![Frecuencias de la señal filtrada](https://github.com/user-attachments/assets/efb07629-fcbc-44f2-956e-a79cd37a0ccf)

En este ejemplo se implementó un filtro IIR Butterworth pasa altos con una frecuencia de corte de 1300 Hz.
