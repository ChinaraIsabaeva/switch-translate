# -*- coding: utf-8 -*-

from letters import eng_letters, ru_letters

def eng_translate(text):
    rus_text = ''
    for char in text:
        rus_text += eng_letters[char]
    return rus_text

def ru_translate(text):
    eng_text = ''
    for char in text:
        eng_text += ru_letters[char]
    return eng_text
