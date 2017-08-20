'''
Created on 19 ago. 2017

@author: bermu
'''
import unittest
import numpy as np
from imagesmanager import Imagesmanager
from numpy import loadtxt

class Test(unittest.TestCase):
    # las direcciones
    path_list = ["Muestras/s1/1.pgm","Muestras/s1/2.pgm", "Muestras/s1/3.pgm", "Muestras/s1/4.pgm", "Muestras/s1/5.pgm", "Muestras/s1/6.pgm","Muestras/s1/7.pgm","Muestras/s1/8.pgm","Muestras/s1/9.pgm","Muestras/s1/10.pgm"]
    # las matrices de las imagenes, cada una corresponde a una imagen, del sujeto s1 
    expected = [np.loadtxt("Pruebas/s1 matrizImg/1"),np.loadtxt("Pruebas/s1 matrizImg/2"),np.loadtxt("Pruebas/s1 matrizImg/3"),np.loadtxt("Pruebas/s1 matrizImg/4"),np.loadtxt("Pruebas/s1 matrizImg/5"),np.loadtxt("Pruebas/s1 matrizImg/6"),np.loadtxt("Pruebas/s1 matrizImg/7"),np.loadtxt("Pruebas/s1 matrizImg/8"),np.loadtxt("Pruebas/s1 matrizImg/9"),np.loadtxt("Pruebas/s1 matrizImg/10")]
    # matrices transformadas en vectores de cada imagen del sujeto 1 
    expectedt2 = [np.loadtxt("Pruebas/s1 mxv/v1"),np.loadtxt("Pruebas/s1 mxv/v2"),np.loadtxt("Pruebas/s1 mxv/v3"),np.loadtxt("Pruebas/s1 mxv/v4"),np.loadtxt("Pruebas/s1 mxv/v5"),np.loadtxt("Pruebas/s1 mxv/v6"),np.loadtxt("Pruebas/s1 mxv/v7"),np.loadtxt("Pruebas/s1 mxv/v8"),np.loadtxt("Pruebas/s1 mxv/v9"),np.loadtxt("Pruebas/s1 mxv/v10")]
    # muestras sin ser transpuestas, es cada sujeto, s1, s2, s3 
    samples = [np.loadtxt("Pruebas/MuestrasSinTransponer/s1"),np.loadtxt("Pruebas/MuestrasSinTransponer/s2"),np.loadtxt("Pruebas/MuestrasSinTransponer/s3"),np.loadtxt("Pruebas/MuestrasSinTransponer/s4"),np.loadtxt("Pruebas/MuestrasSinTransponer/s5"),np.loadtxt("Pruebas/MuestrasSinTransponer/s6"),np.loadtxt("Pruebas/MuestrasSinTransponer/s7"),np.loadtxt("Pruebas/MuestrasSinTransponer/s8"),np.loadtxt("Pruebas/MuestrasSinTransponer/s9"),np.loadtxt("Pruebas/MuestrasSinTransponer/s10")]
    # muestras transpuestas
    samplesTranposed = [np.loadtxt("Pruebas/MuestrtasTranspuestas/s1"),np.loadtxt("Pruebas/MuestrtasTranspuestas/s2"),np.loadtxt("Pruebas/MuestrtasTranspuestas/s3"),np.loadtxt("Pruebas/MuestrtasTranspuestas/s4"),np.loadtxt("Pruebas/MuestrtasTranspuestas/s5"),np.loadtxt("Pruebas/MuestrtasTranspuestas/s6"),np.loadtxt("Pruebas/MuestrtasTranspuestas/s7"),np.loadtxt("Pruebas/MuestrtasTranspuestas/s8"),np.loadtxt("Pruebas/MuestrtasTranspuestas/s9"),np.loadtxt("Pruebas/MuestrtasTranspuestas/s10")]
    #expectedcov = np.loadtxt("Pruebas/cov s1-10")
    G = 0 
    
    def test_addImages(self):
        """
        @summary: This function is an unit test for add images of the class Imagesmanager
        
        Parameters
        ----------
        @param self: part of OOP syntax
        
        Returns
        ----------
        @return: void
        """
        self.G = 0 
        imagesm = Imagesmanager()
        for path in self.path_list:    
            result = Imagesmanager.addImage(imagesm, path)
            result = result.astype('float')
            
            self.assertEqual(result.all(), self.expected[self.G].all(), "No calza")
            
            print(self.G)
            self.G = self.G + 1  
            
    def test_matrix2vector(self):
        """
        @summary: This function is an unit test for matrix2vector of the class Imagesmanager
        
        Parameters
        ----------
        @param self: part of OOP syntax
        
        Returns
        ----------
        @return: void
        """
        imagesm = Imagesmanager()
        self.G = 0 
        for mat in self.expected:    
            result = imagesm.matrix2vector(mat)
            result = result.astype('float')
            
            self.assertEqual(result.all(), self.expectedt2[self.G].all(), "No calza")
            
            print(self.G+10)
            self.G = self.G + 1  
        
        
    def test_transpose(self):
        """
        @summary: This function is an unit test for transpose of the class Imagesmanager
        
        Parameters
        ----------
        @param self: part of OOP syntax
        
        Returns
        ----------
        @return: void
        """
        imagesm = Imagesmanager()
        self.G = 0 
        for muestra in self.samples:  
              
            result = imagesm.transpose(muestra)
            result = result.astype('float')
            
            self.assertEqual(result.all(), self.samplesTranposed[self.G].all(), "No calza")
            
            print(self.G+20)
            self.G = self.G + 1
              
"""   
    def test_cov(self):
        
        @summary: This function is an unit test for calculating covariance matrix of the class Imagesmanager
        
        Parameters
        ----------
        @param self: part of OOP syntax
        
        Returns
        ----------
        @return: void
        
        imagesm = Imagesmanager()
        
        self.G = 0 
      
           
        result = imagesm.calculateCovarianceMatrix(np.loadtxt("Pruebas/muestra s1-10"))
        
        self.assertEqual(result.all(), self.expectedcov.all(), "No son la misma matriz despues de ser transpuestos")
        print("Listo test cov")
"""       
            
        