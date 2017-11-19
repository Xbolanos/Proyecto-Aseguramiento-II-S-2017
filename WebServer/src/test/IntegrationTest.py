'''
Created on Nov 17, 2017

@author: erickhdez
'''
import unittest
from controller import facade
from django.core.files.uploadedfile import SimpleUploadedFile
from random import randint


class Test(unittest.TestCase):
    subjects_count = 5

    def test_1_sign_in(self):
        notUser = {
            'email': 'e@a.com',
            'password': '123'}

        user = {
            'email': 'admin@reconoceme.com',
            'password': '123Queso'}

        notObject = None

        self.assertFalse(facade.signin(notUser))
        self.assertFalse(facade.signin(notObject))
        self.assertTrue(facade.signin(user))

    def test_2_training(self):
        autovectors = 100
        images_per_subject = 8
        files = {}
        filesData = {}
        filesCount = 1

        for i in range(1, Test.subjects_count + 1):
            for j in range(1, images_per_subject + 1):
                file = open('Muestras/S' + str(i) + '/' + str(j) + '.pgm',
                            'rb')
                simpleFile = SimpleUploadedFile(str(j) + '.pgm',
                                                file.read(),
                                                'image/x-portable-graymap')
                files['file' + str(filesCount)] = simpleFile
                filesData['file' + str(filesCount) + 'data'] = 'S' + str(i)

                file.close()
                filesCount += 1

        result = facade.train_system(files,
                                     filesData,
                                     autovectors,
                                     images_per_subject)

        self.assertTrue(result)

    def test_3_recognize_centroid(self):
        subject = randint(1, Test.subjects_count)
        image = randint(8, 10)
        file = open('Muestras/S' + str(subject) + '/' + str(image) + '.pgm',
                    'rb')

        simpleFile = SimpleUploadedFile(str(image) + '.pgm',
                                        file.read(),
                                        'image/x-portable-graymap')

        noneFile = None
        wrongInstance = {}

        result1 = facade.recognize_subject(simpleFile, 0)
        expected1 = 'S' + str(subject)

        result2 = facade.recognize_subject(noneFile, 0)
        expected2 = 'error'

        result3 = facade.recognize_subject(wrongInstance, 0)
        expected3 = 'error'

        self.assertEqual(expected1, result1[3])
        print('Result1: ' + result1[1])
        self.assertEqual(expected2, result2[0], result1[1])
        print('Result2: ' + result2[1])
        self.assertEqual(expected3, result3[0], result1[1])
        print('Result3: ' + result3[1])

    def test_4_recognize_k_neighbors(self):
        subject = randint(1, self.subjects_count)
        image = randint(8, 10)
        file = open('Muestras/S' + str(subject) + '/' + str(image) + '.pgm',
                    'rb')

        simpleFile = SimpleUploadedFile(str(image) + '.pgm',
                                        file.read(),
                                        'image/x-portable-graymap')

        result = facade.recognize_subject(simpleFile)
        expected = 'S' + str(subject)

        self.assertEqual(expected, result)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
