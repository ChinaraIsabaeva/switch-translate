# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

letters = {'q': 'й', 'w': 'ц', 'e' :'у', 'r' :'к', 't' :'е', 'y' :'н', 'u' :'г', 'i' :'ш', 'o' :'щ', 'p' :'з', '[' :'х', ']' :'ъ', 'a' :'ф', 's' :'ы', 'd' :'в', 'f' :'а', 'g' :'п', 'h' :'р', 'j' :'о', 'k' :'л', 'l' :'д', ';' :'ж', "'" :'э', 'z' :'я', 'x' :'ч', 'c' :'с', 'v' :'м', 'b' :'и', 'n' :'т', 'm' :'ь', ',' :'б', '.' :'ю', '/': '.', '!': '!', '@': '"', '#': '№', '$': ';', '%': '%', '^': ':', '&': '?', '*': '*', '(': '(', ')': ')', ' ': ' ', 'Q': 'Й', 'W': 'Ц', 'E' :'У', 'R' :'К', 'T' :'Е', 'Y' :'Н', 'U' :'Г', 'I' :'Ш', 'O' :'Щ', 'P' :'З', '{' :'Х', '}' :'Ъ', 'A' :'Ф', 'S' :'Ы', 'D' :'В', 'F' :'А', 'G' :'П', 'H' :'Р', 'J' :'O', 'K' :'Л', 'L' :'Д', ':' :'Ж', '"' :'Э', 'Z' :'Я', 'X' :'Ч', 'C' :'С', 'V' :'М', 'B' :'И', 'N' :'Т', 'M' :'Ь', '<' :'Б', '>' :'Ю', '?': '.'}

def translate(text):
    rus_text = ''
    for char in text:
        rus_text += letters[char]
    return rus_text

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def my_form_post():
    data = request.get_json()
    result = translate(data[u'text'])
    return result

if __name__ == '__main__':
    app.run()
