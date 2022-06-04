import unittest
from translator import * 
class TestTranslator(unittest.TestCase):
   def test_en_to_fr(self):
       self.assertEqual(en_to_fr("Hello"), "Bonjour")
       self.assertNotEqual(en_to_fr("Hello"),"Bonjour")
 
   def test_fr_to_en(self):
       self.assertEqual(fr_to_en("Bonjour"), "Hello")
       self.assertNotEqual(fr_to_en("Bonjour"), "Hello")
 
if __name__ == '__main__':
   unittest.main()