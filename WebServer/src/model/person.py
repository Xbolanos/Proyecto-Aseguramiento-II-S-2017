'''
Created on Oct 10, 2017

@author: epikhdez
'''


class Person():
    '''
    @summary: class to hold up the subjects ID and wanted state so the system
    knows to whom belongs the face and raise and alert in case the subject is
    a wanted one.
    '''

    def __init__(self, sid, wanted):
        '''
        @summary: creates a new instance for this class.

        Params
        ------
        @param sid: the related subject id, usually its position in the faces
        global array.
        @param wanted: the subject's wanted state.
        '''
        self.sid = sid
        self.wanted = wanted
