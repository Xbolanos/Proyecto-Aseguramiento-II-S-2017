import numpy as np 
import cv2
from matplotlib import pyplot as plt
# las imagenes estan ya en vector pero falta trasponerlas 
#como necesitamos las muestras en las columnas y no en las filas como esta
images = []
A = []
def addImage(path):
    imgMatrix = cv2.imread(path,0)
    #sacamos el vector de la imagen
    vector = np.asarray(imgMatrix).reshape(-1)
    images.append(vector) 
        
print (cv2.__version__)
addImage('2.jpg')
addImage('3.jpg')

def analysis():
    return np.array(images).transpose()

A = analysis()
print(A)

#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()

