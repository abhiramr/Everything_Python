import unittest
from math import factorial as fact
def facto(n):
    if n < 0:
        return -1
    else:
        return fact(n)
        
class factUnitTest(unittest.TestCase):
    def setup(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_positive_fact(self):
        self.assertNotEqual(facto(11),-1)
        self.assertNotEqual(facto(0),-1)
        self.assertNotEqual(facto(23),-1)
    
    def test_negative_fact(self):
        self.assertEqual(facto(-34),-1)
        
if __name__=="__main__":
    unittest.main()
