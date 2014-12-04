# -*- coding: utf-8 -*-

import os
import unittest
import switch_translate
from flask import json
from lib.translate import eng_translate, ru_translate

class TranslitTestCase(unittest.TestCase):
    def setUp(self):
        self.text_one = u'ghjdthrf heccrjuj ntrcnf'
        self.text_two = u'срусл утпдшыр еуче'
   
    def test_one(self):
        result = eng_translate(self.text_one)
        self.assertEqual(result, 'проверка русского текста')

    def test_two(self):
        result = ru_translate(self.text_two)
        self.assertEqual(result, 'check english text')


class Switch_tranlateTestCase(unittest.TestCase):
    def setUp(self):
        self.app = switch_translate.app.test_client()
        self.text_one = 'ghjdthztv heccrbq ntrcn'
        self.text_two = u'срусл утпдшыр еуче'

    def test_eng(self):
        response = self.app.post('/', data=json.dumps({'text':  self.text_one}), content_type='application/json')
        self.assertEquals(response.get_data(), 'проверяем русский текст') 

    def test_ru(self):
        response = self.app.post('/ru', data=json.dumps({'text':  self.text_two}), content_type='application/json')
        self.assertEquals(response.get_data(), 'check english text') 
      
if __name__ == '__main__':
    unittest.main()
