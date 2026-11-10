import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Ramirez Azul NC 0441
print("Ramirez Azul NC 0441")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro VA")
mi_iagen = cv2.imread('taehbb.jpg')
plt.imshow(mi_iagen)
plt.title('Taehyung y Ramirez Azul NC 0441')
plt.show()

print("-+-+-+ Puntos en la imagen +-+-+-+")
plt.imshow(mi_iagen)
x = [100,100,200]
y = [100,400,200]
plt.scatter(x ,y, s=20, c='red')
plt.show()


