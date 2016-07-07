import unittest
from mainThread import MainThread

class TestCase(unittest.TestCase):
 
    def test_set(self):
    	thread = MainThread()
        setDict = thread.setDict('a','b')
        self.assertEquals("OK", setDict)

if __name__ == '__main__':
        unittest.main()