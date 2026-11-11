import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Ramirez Azul NC 0441
print("Ramirez Azul NC 0441")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro VA")
mi_iagen = cv2.imread('taehbb.jpg')
mi_iagen = cv2.cvtColor(mi_iagen, cv2.COLOR_BGR2RGB) # Convertir BGR a RGB para Matplotlib
plt.imshow(mi_iagen)
plt.title('Taehyung y Ramirez Azul NC 0441')
plt.show()

print("-+-+-+ Puntos en la imagen +-+-+-+")
plt.imshow(mi_iagen)
x = [100,100,200]
y = [100,400,200]
plt.scatter(x ,y, s=20, c='red')
plt.show()

print("+-+-+ Cuadro azul en la imagen +-+-+")
img_taeh = cv2.imread('taehbb.jpg')
img_taeh = cv2.cvtColor(img_taeh, cv2.COLOR_BGR2RGB) 
plt.imshow(img_taeh)
x = [10, 360, 360, 10, 10]
y = [100, 100, 520, 520, 100]
plt.plot(x ,y, c='blue')
plt.show()

print("+-+-+ Circulo verde en la imagen +-+-+")
I = cv2.imread('taehbb.jpg')
I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB) # Convertir BGR a RGB
plt.imshow(I)

N = 30 # lados del poligono
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc, yc) = (340, 320)
r = 150 # radio

for i in range(N+1):
    t = 2*np.pi/N*i
    x[i] = xc + r*np.cos(t) 
    y[i] = yc + r*np.sin(t) 

plt.plot(x, y, c='green') 
plt.show()