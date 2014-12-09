# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from lib.translate import translate

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        text = data[u'text']
        result = translate(text)
        return result
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
