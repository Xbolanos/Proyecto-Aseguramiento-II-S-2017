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

    def test_1_sign_in_not_user(self):
        notUser = {
            'email': 'e@a.com',
            'password': '123'}

        self.assertFalse(facade.signin(notUser))
        print('Sing in con un usuario no registrado.')

    def test_2_sign_in_wrong_password(self):
        user = {
            'email': 'admin@reconoceme.com',
            'password': '123'}

        self.assertFalse(facade.signin(user))
        print('Sing in con un usuario registrado, pero contraseña incorrecta.')

    def test_3_sign_in_user(self):
        user = {
            'email': 'admin@reconoceme.com',
            'password': '123Queso'}

        self.assertTrue(facade.signin(user))
        print('Sing in con un usuario registrado legitimo.')

    def test_4_training(self):
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
        print('Entrenamiento básico del sistema.')

    def test_5_recognize_centroid(self):
        subject = randint(1, Test.subjects_count)
        image = randint(8, 10)
        file = open('Muestras/S' + str(subject) + '/' + str(image) + '.pgm',
                    'rb')

        simpleFile = SimpleUploadedFile(str(image) + '.pgm',
                                        file.read(),
                                        'image/x-portable-graymap')

        result1 = facade.recognize_subject(simpleFile, 0)
        expected1 = 'S' + str(subject)

        subject = randint(1, Test.subjects_count)
        image = randint(8, 10)
        file = open('Muestras/S' + str(subject) + '/' + str(image) + '.pgm',
                    'rb')

        simpleFile = SimpleUploadedFile(str(image) + '.pgm',
                                        file.read(),
                                        'image/x-portable-graymap')

        result2 = facade.recognize_subject(simpleFile, 0)
        expected2 = 'S' + str(subject)

        self.assertEqual(expected1, result1[3])
        print('Result1: ' + result1[1])

        self.assertEqual(expected2, result2[3])
        print('Result2: ' + result2[1])

    def test_6_recognize_k_neighbors(self):
        subject = randint(1, Test.subjects_count)
        image = randint(8, 10)
        file = open('Muestras/S' + str(subject) + '/' + str(image) + '.pgm',
                    'rb')

        simpleFile = SimpleUploadedFile(str(image) + '.pgm',
                                        file.read(),
                                        'image/x-portable-graymap')

        result1 = facade.recognize_subject(simpleFile, 1)
        expected1 = 'S' + str(subject)

        subject = randint(1, Test.subjects_count)
        image = randint(8, 10)
        file = open('Muestras/S' + str(subject) + '/' + str(image) + '.pgm',
                    'rb')

        simpleFile = SimpleUploadedFile(str(image) + '.pgm',
                                        file.read(),
                                        'image/x-portable-graymap')

        result2 = facade.recognize_subject(simpleFile, 1)
        expected2 = 'S' + str(subject)

        self.assertEqual(expected1, result1[3])
        print('Result1: ' + result1[1])

        self.assertEqual(expected2, result2[3])
        print('Result2: ' + result2[1])


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
