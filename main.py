# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 08:52:08 2020

@author: sami
"""

from flask import Flask, request, render_template
app = Flask(__name__)
import os
from flask import send_from_directory
from textsummarizer import getsummary

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/")
def hello():
    return render_template('summarize.html')
 
@app.route("/summarize", methods=['POST'])
def echo(): 
    summary=getsummary(request.form['text'])
    print(summary)
    return render_template('summarize.html', text=summary)

if __name__ == "__main__":
    app.run()