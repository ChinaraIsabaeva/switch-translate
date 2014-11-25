# -*- coding: utf-8 -*-

import os
import unittest

letters = {'q': 'й', 'w': 'ц', 'e' :'у', 'r' :'к', 't' :'е', 'y' :'н', 'u' :'г', 'i' :'ш', 'o' :'щ', 'p' :'з', '[' :'х', ']' :'ъ', 'a' :'ф', 's' :'ы', 'd' :'в', 'f' :'а', 'g' :'п', 'h' :'р', 'j' :'о', 'k' :'л', 'l' :'д', ';' :'ж', "'" :'э', 'z' :'я', 'x' :'ч', 'c' :'с', 'v' :'м', 'b' :'и', 'n' :'т', 'm' :'ь', ',' :'б', '.' :'ю', '/': '.', '!': '!', '@': '"', '#': '№', '$': ';', '%': '%', '^': ':', '&': '?', '*': '*', '(': '(', ')': ')', ' ': ' ', 'Q': 'Й', 'W': 'Ц', 'E' :'У', 'R' :'К', 'T' :'Е', 'Y' :'Н', 'U' :'Г', 'I' :'Ш', 'O' :'Щ', 'P' :'З', '{' :'Х', '}' :'Ъ', 'A' :'Ф', 'S' :'Ы', 'D' :'В', 'F' :'А', 'G' :'П', 'H' :'Р', 'J' :'O', 'K' :'Л', 'L' :'Д', ':' :'Ж', '"' :'Э', 'Z' :'Я', 'X' :'Ч', 'C' :'С', 'V' :'М', 'B' :'И', 'N' :'Т', 'M' :'Ь', '<' :'Б', '>' :'Ю', '?': '.', '-': '-'}

def translate(text):
    rus_text = ''
    for char in text:
        rus_text += letters[char]
    return rus_text

class TestSequenceFunctions(unittest.TestCase):
   def setUp(self):
        self.text_one = 'dfhnfyjq vjq gntyxbr? f z tuj czirf'
        self.text_two = "B nfr yflj gjghj,jdfnm lkbyysq ntrcn? c 'ynthjv\nnf-c yt pf,eltv ghj nbht"
   
   def test_one(self):
      translate(self.text_one)
      self.assertEqual(self.text_one, 'dfhnfyjq vjq gntyxbr? f z tuj czirf')
      
if __name__ == '__main__':
    unittest.main()
