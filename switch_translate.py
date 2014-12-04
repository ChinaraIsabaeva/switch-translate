# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from lib.translate import eng_translate, ru_translate

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        text = data[u'text']
        if '\n' in text:
            index = text.index('\n')
            text = text.replace('\n', '')
            new_text = eng_translate(text)
            result = new_text[:index] + '\n' + new_text[index:]
        else:
            result = eng_translate(text)
        return result
    else:
        return render_template('home.html')

@app.route('/ru', methods=['GET', 'POST'])
def ru():
    if request.method == 'POST':
        data = request.get_json()
        text = data[u'text']
        if '\n' in text:
            index = text.index('\n')
            text = text.replace('\n', '')
            new_text = ru_translate(text)
            result = new_text[:index] + '\n' + new_text[index:]
        else:
            result = ru_translate(text)
        return result
    else:
        return render_template('russian.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
