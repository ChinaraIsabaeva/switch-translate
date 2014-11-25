# -*- coding: utf-8 -*-

import os
import unittest

letters = {'q': 'й', 'w': 'ц', 'e' :'у', 'r' :'к', 't' :'е', 'y' :'н', 'u' :'г', 'i' :'ш', 'o' :'щ', 'p' :'з', '[' :'х', ']' :'ъ', 'a' :'ф', 's' :'ы', 'd' :'в', 'f' :'а', 'g' :'п', 'h' :'р', 'j' :'о', 'k' :'л', 'l' :'д', ';' :'ж', "'" :'э', 'z' :'я', 'x' :'ч', 'c' :'с', 'v' :'м', 'b' :'и', 'n' :'т', 'm' :'ь', ',' :'б', '.' :'ю', '/': '.', '!': '!', '@': '"', '#': '№', '$': ';', '%': '%', '^': ':', '&': '?', '*': '*', '(': '(', ')': ')', ' ': ' ', '?': ','}

def translate(text):
    rus_text = ''
    for char in text:
        rus_text += letters[char]
    return rus_text

class TestSequenceFunctions(unittest.TestCase):
   def setUp(self):
        self.text_str = 'dfhnfyjq vjq gntyxbr? f z tuj czirf'
        self.text_uni = u'dfhnfyjq vjq gntyxbr? f z tuj czirf'
   
   def test_str(self):
      translate(self.text_str)
      self.assertEqual(self.text_str, 'dfhnfyjq vjq gntyxbr? f z tuj czirf')

   def test_uni(self):
      translate(self.text_uni)
      self.assertEqual(self.text_uni, u'dfhnfyjq vjq gntyxbr? f z tuj czirf')
      
if __name__ == '__main__':
    unittest.main()
