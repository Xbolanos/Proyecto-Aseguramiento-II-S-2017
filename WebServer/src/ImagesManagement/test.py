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
    # las matrices de las imagenes
    expected = [np.loadtxt("0"),np.loadtxt("1"),np.loadtxt("2"),np.loadtxt("3"),np.loadtxt("4"),np.loadtxt("5"),np.loadtxt("6"),np.loadtxt("7"),np.loadtxt("8"),np.loadtxt("9")]
    # matrices transformadas en vectores 
    expectedt2 = [np.loadtxt("10"),np.loadtxt("11"),np.loadtxt("12"),np.loadtxt("13"),np.loadtxt("14"),np.loadtxt("15"),np.loadtxt("16"),np.loadtxt("17"),np.loadtxt("18"),np.loadtxt("19")]
    # muestras sin ser transpuestas 
    samples = [np.loadtxt("30"),np.loadtxt("31"),np.loadtxt("32"),np.loadtxt("33"),np.loadtxt("34"),np.loadtxt("35"),np.loadtxt("36"),np.loadtxt("37"),np.loadtxt("38"),np.loadtxt("39")]
    # muestras transpuestas
    samplesTranposed = [np.loadtxt("20"),np.loadtxt("21"),np.loadtxt("22"),np.loadtxt("23"),np.loadtxt("24"),np.loadtxt("25"),np.loadtxt("26"),np.loadtxt("27"),np.loadtxt("28"),np.loadtxt("29")]
    expectedCovarianceMatrix=[]
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
              
    def calculateCovarianceMatrix(self):
        """
        @summary: This function is an unit test for calculateCovarianceMatrix of the class Imagesmanager
        
        Parameters
        ----------
        @param self: part of OOP syntax
        
        Returns
        ----------
        @return: void
        """
        self.G = 0 
        imagesm = Imagesmanager()
        for sampleTransposted in self.samplesTranposed:    
            result = imagesm.calculateCovarianceMatrix(sampleTransposted)
            result = result.astype('float')
            
            self.assertEqual(result.all(), self.expectedCovarianceMatrix[self.G].all(), "No calza")
            
            print(self.G)
            self.G = self.G + 1
            
        