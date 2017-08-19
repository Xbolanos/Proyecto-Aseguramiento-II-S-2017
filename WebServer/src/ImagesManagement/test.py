'''
Created on 19 ago. 2017

@author: bermu
'''
import unittest
import numpy as np
from imagesmanager import Imagesmanager
from numpy import loadtxt

class Test(unittest.TestCase):
    path_images = "Muestras/s1/1.pgm"
    path_list = ["Muestras/s1/1.pgm","Muestras/s1/2.pgm", "Muestras/s1/3.pgm", "Muestras/s1/4.pgm", "Muestras/s1/5.pgm", "Muestras/s1/6.pgm","Muestras/s1/7.pgm","Muestras/s1/8.pgm","Muestras/s1/9.pgm","Muestras/s1/10.pgm"]
    expected = [np.loadtxt("0"),np.loadtxt("1"),np.loadtxt("2"),np.loadtxt("3"),np.loadtxt("4"),np.loadtxt("5"),np.loadtxt("6"),np.loadtxt("7"),np.loadtxt("8"),np.loadtxt("9")]
    expectedt2 = [np.loadtxt("10"),np.loadtxt("11"),np.loadtxt("12"),np.loadtxt("13"),np.loadtxt("14"),np.loadtxt("15"),np.loadtxt("16"),np.loadtxt("17"),np.loadtxt("18"),np.loadtxt("19")]
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