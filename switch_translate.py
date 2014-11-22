# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template

letters = {'q': 'й', 'w': 'ц', 'e' :'у', 'r' :'к', 't' :'е', 'y' :'н', 'u' :'г', 'i' :'ш', 'o' :'щ', 'p' :'з', '[' :'х', ']' :'ъ', 'a' :'ф', 's' :'ы', 'd' :'в', 'f' :'а', 'g' :'п', 'h' :'р', 'j' :'о', 'k' :'л', 'l' :'д', ';' :'ж', "'" :'э', 'z' :'я', 'x' :'ч', 'c' :'с', 'v' :'м', 'b' :'и', 'n' :'т', 'm' :'ь', ' ,' :'б', '.' :'ю', '/': '.', '!': '!', '@': '"', '#': '№', '$': ';', '%': '%', '^': ':', '&': '?', '*': '*', '(': '(', ')': ')', ' ': ' '}

def translate(text):
    rus_text = ''
    for char in text:
        
        rus_text += letters[char]
    return rus_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        result = translate(text)
        return render_template('home.html', result=result)
    else:
        return render_template('home.html')


def my_form_post():
    
    return render_template('home.html', result=result)
    

if __name__ == '__main__':
    app.run()
