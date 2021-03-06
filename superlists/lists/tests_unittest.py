from django.test import TestCase

from unittest import mock
import os
import tempfile

from lists.utils import RemovalService


def add(a, b):
    '''
    additing the given two values
    '''
    return a + b


class SimpleTest(TestCase):

    def setUp(self):
        self.tmpfile = os.path.join(tempfile.gettempdir(), "dummy.txt")

        with open(self.tmpfile, "wb") as f:
            f.write(b"Hello Guys.")

        print("File:{}".format(self.tmpfile))
        

    def test_basic_arithmatic(self):
        '''
        Testcase for basic arithmatic addition function
        '''
        self.assertEquals(2, add(1, 1))

    def test_file_remover_withoutmock(self):
        '''
        Testcase for api method
        '''
        obj = RemovalService()
        obj.rm(self.tmpfile)

        self.assertFalse(os.path.isfile(self.tmpfile), "Unable to remove files.")
        
    @mock.patch('lists.utils.os')
    def test_file_remover_withmock(self, mock_os):
        '''                                                                                                                                                                                                        Testcase for api method                                                                                                                                                                                    '''
        obj = RemovalService()
        mock_os.path = mock.MagicMock()
        mock_os.path.isfile.return_value = False
       
        obj.rm("any path")

        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

        # make the file 'exist'
        mock_os.path.isfile.return_value = True
          
        obj.rm("any path")
    
        mock_os.remove.assert_called_with("any path")
        
        
