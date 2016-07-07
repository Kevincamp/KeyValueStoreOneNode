import unittest
from mainThread import MainThread

class TestCase(unittest.TestCase):
 	cache = {[a:b]} # variable de clase
    def test_set(self):
    	thread = MainThread()
        setDict = thread.setDict('a','b')
        self.assertEquals("OK", setDict)
    def test_set2(self):
    	thread = MainThread()
    	setDict = thread.setDict('b','')
    	self.assertEquals("OK", setDict)
    def test_thread(self):
    	thread = create_autospec(MainThread)
    	

if __name__ == '__main__':
        unittest.main()