'''
Created on Nov 17, 2017

@author: erickhdez
'''
import unittest
from controller import facade
from django.core.files.uploadedfile import SimpleUploadedFile
from random import randint


class Test(unittest.TestCase):
    def test_1_sign_in(self):
        notUser = {
            'email': 'e@a.com',
            'password': '123'}

        user = {
            'email': 'admin@reconoceme.com',
            'password': '123Queso'}

        self.assertFalse(facade.signin(notUser))
        self.assertTrue(facade.signin(user))

    def test_2_training(self):
        autovectors = 100
        images_per_subject = 8
        files = {}
        filesData = {}
        filesCount = 1

        for i in range(1, 6):
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

    def test_3_recognize(self):
        subject = randint(1, 5)
        image = randint(1, 10)
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
