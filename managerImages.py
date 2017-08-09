import numpy as np 
import cv2
from matplotlib import pyplot as plt

#vamos a pasar la imagen que es matriz a vector 
def img2vector(img):
    vector = []
    datos = img.shape
    for x in range (0, datos[0]):
        for y in range (0, datos[1]):
            vector.append(img[x,y])
    return vector 


#transformar de vectores a matriz A vista en clase
def muestras2matriz(vectores):
    matriz = []
    # p = m x n : que es la cantidad de pixeles que tiene 
    p = len(vectores[0])
    # r = k x s : k muestras por s sujetos 
    r = len(vectores)
    for x in range(0, p):
        nuevaFila = []
        for y in range(0, r):
            nuevaFila.append(vectores[y][x]) 
        matriz.append(nuevaFila)
    return matriz
             
        
print (cv2.__version__)
img = cv2.imread('2.jpg',0)
img2 = cv2.imread('3.jpg',0)

#sacamos el vector de la imagen
v = img2vector(img)
v2 = img2vector(img2)
#con mean se calcula la media gracias a numpy
#print ("la media, badumtss")
#print (np.array(v).mean())

#dados los vectores de las imagenes, sacamos la matriz de covarianza
#vectores = np.vstack((v, v2))
#print(np.cov(vectores))

print (muestras2matriz([v,v2]))
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


