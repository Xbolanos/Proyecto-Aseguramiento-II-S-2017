import numpy as np 
import cv2
from matplotlib import pyplot as plt


# las imagenes estan ya en vector pero falta trasponerlas 
#como necesitamos las muestras en las columnas y no en las filas como esta
images = []
A = []
def addImage(path):
    return cv2.imread(path,0)
   
     
#sacamos el vector de la imagen
def matrix2vector(matrix):        
    return np.asarray(matrix).reshape(-1)

#vamos a meter cada vector en image, image es casi la matriz
# A que vimos en clase, que tiene todas las muestras
def add2images(vector):
    images.append(vector)

#le da vuelta a image, que ya volveria cada muestra en columna (: 
def analysis():
    return np.array(images).transpose()

#esto eventualmente cambiara para cuando tengamos lo web 
def process():
    print (cv2.__version__)
    add2images(matrix2vector(addImage('2.jpg')))
    add2images(matrix2vector(addImage('3.jpg')))
    A = analysis() #aqui se crea la matriz de muestras
    print(A)
    
process()







#---------------------------------------------------------------------
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()






