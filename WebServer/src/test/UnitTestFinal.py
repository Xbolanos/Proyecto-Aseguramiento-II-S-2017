'''
Created on 11 nov. 2017

@author: bermu
'''
import unittest
import numpy as np
from WebServer.settings import STATICFILES_DIRS
from controller.images_manager import ImagesManager
from controller.faces_manager import FacesManager


class Test(unittest.TestCase):
    test_4_centroid = np.array([[5,8,15,21],[5,8,15,21],[5,8,15,21],[5,8,15,21]])
    prueba = [ np.array([[4],[4],[4],[4]]), 
              np.array([[10],[10],[10],[10]]),
              np.array([[16],[16],[16],[16]]),
              np.array([[30],[30],[30],[30]])
              ]
    prueba2 = [1,2,3,4]
    
    
    test_k = np.array([[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,
                        24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40],
                       [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,
                        24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40],
                       [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,
                        24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40],
                       [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,
                        24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]])
    
    
    prueba_k = [ np.array([[4],[4],[4],[4]]), 
              np.array([[14],[14],[14],[14]]),
              np.array([[24],[24],[24],[24]]),
              np.array([[45],[45],[45],[45]])
              ]
    test_min = [ np.array([65,7,34,8]),
                np.array([1,2,3,4]),
                np.array([455,488,0,2000]),
                np.array([1000,1000,1000,0])
                ]
    expected_min = [ np.array([65,50000000,34,8]),
                np.array([50000000,2,3,4]),
                np.array([455,488,50000000,2000]),
                np.array([1000,1000,1000,50000000])
        ]
    
    test_person = [4,15,23,28]

    def test_nearest_centroid(self):
        G = 0
        FacesManager.change_images_per_person(1)
        for i in self.prueba:
            result = FacesManager.classify_nearest_centroid(i, self.test_4_centroid)
            expected = self.prueba2[G]
            err = "Mismatch of nearest centroid"
            self.assertEqual(result, expected, err)
            print("Nearest centroid unittest: " + str(G))
            G = G + 1
            
    def test_nearest_centroid_dif(self):
        exception = "some params of centroid don't match"
        with self.assertRaisesRegexp(Exception, exception):
            FacesManager.classify_nearest_centroid(self.prueba, "o")
        print("Nearest centroid dif unittest: raise specific exception")
        with self.assertRaisesRegexp(Exception, exception):
            FacesManager.classify_nearest_centroid("o", self.test_4_centroid)
        print("Nearest centroid dif unittest: raise specific exception")

    def test_nearest_centroid_null(self):
        exception = "some params of centroid are null"
        with self.assertRaisesRegexp(Exception, exception):
            FacesManager.classify_nearest_centroid(self.prueba, None)
        print("Nearest centroid null unittest: raise specific exception")
        with self.assertRaisesRegexp(Exception, exception):
            FacesManager.classify_nearest_centroid(None, self.test_4_centroid)
        print("Nearest centroid null unittest: raise specific exception")

    def test_k_neighbors(self):
        FacesManager.change_images_per_person(10)
        G = 0
        while (G < 4):
            result = FacesManager.k_neighbors(3,
                                              self.prueba_k[G],
                                              self.test_k)
            expected = self.prueba2[G]
            err = "Mismatch of k neighbors"
            self.assertEqual(result, expected, err)
            print("K neighbors unittest: " + str(G))
            G = G + 1

    def test_k_neighbors_dif(self):
        exception = "some params of k-neighborhs don't match"
        with self.assertRaisesRegexp(Exception, exception):
            FacesManager.k_neighbors(3, self.prueba_k[0], "o")
        print("K neighbors dif unittest: raise specific exception")
        with self.assertRaisesRegexp(Exception, exception):
            FacesManager.k_neighbors(3, "o", self.test_k)
        print("K neighbors dif unittest: raise specific exception")
        with self.assertRaisesRegexp(Exception, exception):
            FacesManager.k_neighbors("o", self.prueba_k[0], self.test_k)
        print("K neighbors dif unittest: raise specific exception")

    def test_k_neighbors_null(self):
        exception = "some params of k neighbors are null"
        with self.assertRaisesRegexp(Exception, exception):
            FacesManager.k_neighbors(3, self.prueba_k[0], None)
        print("K neighbors null unittest: raise specific exception")
        with self.assertRaisesRegexp(Exception, exception):
            FacesManager.k_neighbors(3, None, self.test_k)
        print("K neighbors null unittest: raise specific exception")
        with self.assertRaisesRegexp(Exception, exception):
            FacesManager.k_neighbors(None, self.prueba_k[0], self.test_k)
        print("K neighbors null unittest: raise specific exception")

    def test_get_min(self):
        G = 0 
        max = len(self.test_min)
        while(G < max):
            result = FacesManager.get_min(self.test_min[G])[1]
            expected = self.expected_min[G]
            err = "Mismatch of get min"
            self.assertEqual(result.all(), expected.all(), err)
            print("Get min unittest: " + str(G))
            G = G + 1

    def test_get_min_dif(self):
        exception = "distance of get_min doesn't match"
        with self.assertRaisesRegexp(Exception, exception):
            FacesManager.get_min("other")
        print("Get min dif unittest: raise specific exception")

    def test_get_min_null(self):
        exception = "distance of get_min is null"
        with self.assertRaisesRegexp(Exception, exception):
            FacesManager.get_min(None)
        print("Get min null unittest: raise specific exception")

    def test_get_person(self):
        G = 0 
        FacesManager.change_images_per_person(8)
        max = len(self.test_person)
        while(G < max): 
            result = FacesManager.get_person(self.test_person[G])
            expected = self.prueba2[G]
            err = "Mismatch of get person"
            self.assertEqual(result, expected, err)
            print("Get Person unittest: " + str(G))
            G = G + 1

    def test_get_person_dif(self):
        exception = "n of get_person doesn't match"
        with self.assertRaisesRegexp(Exception, exception):
            FacesManager.get_person("other")
        print("Get person dif unittest: raise specific exception")

    def test_get_person_null(self):
        exception = "distance of get_min is null"
        with self.assertRaisesRegexp(Exception, exception):
            FacesManager.get_min(None)
        print("Get min null unittest: raise specific exception")
            