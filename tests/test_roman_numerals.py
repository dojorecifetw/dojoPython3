import unittest
from romanconverter import romanToArabic

class TestRomanNumerals(unittest.TestCase):
    
    def test_I_is_1(self):
        self.assertEqual(romanToArabic('I'), 1)
        
    def test_V_is_5(self):
        self.assertEqual(romanToArabic('V'), 5)
    
    def test_X_is_10(self):
        self.assertEqual(romanToArabic('X'), 10)
        
    def test_L_is_50(self):
        self.assertEqual(romanToArabic('L'), 50)
    
    def test_C_is_100(self):
        self.assertEqual(romanToArabic('C'), 100)
        
    def test_II_is2(self):
        self.assertEqual(romanToArabic('II'), 2)
        
    def test_IV_is_4(self):
       self.assertEqual(romanToArabic('IV'), 4)
        
    def test_IX_is_9(self):
       self.assertEqual(romanToArabic('IX'), 9)
        
    def xtest_XCI_is_91(self):
       self.assertEqual(romanToArabic('XCI'), 91)

    def test_IIII_is_not_4(self):
        self.assertNotEqual(romanToArabic('IIII'), 4)
        
    if __name__ == "__main__":
        unittest.main()