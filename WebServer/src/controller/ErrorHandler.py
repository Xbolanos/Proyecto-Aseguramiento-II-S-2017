'''
Created on 8 nov. 2017

@author: bermu
'''


class ErrorHandler(object):

    def __init__(self):
        '''
        Constructor de la excepcion
        '''
    
    def error(self, message):
        """
        @summary: prints the error because this is the
        error handler
        
        @param: message: the message that throws 
        the exception 
        """
        print(str(message))