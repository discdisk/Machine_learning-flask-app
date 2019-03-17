import os
os.environ['HDF5_DISABLE_VERSION_CHECK']='2'
from flask import Flask, render_template ,request
from data import articals
import base64
import json
import numpy as np
from imageprocess.img_process import preprocess
from imageprocess.MyChainList_gpu import ocr

app = Flask(__name__)
artic=articals()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/p5draw')
def p5draw():
    return render_template('p5draw.html')

@app.route('/sketch.js')
def sketch():
    return render_template('/sketch.js')
@app.route('/gentxt.js')
def gentxt():
    return render_template('/gentxt.js')

@app.route('/Link')
def link():
    return render_template('Link.html')

@app.route('/articals')
def articals():
    return render_template('articals.html',articals=artic)

@app.route('/artical/<string:id>')
def artical(id):
    return render_template('artical.html',idnum=id)

@app.route('/demotext', methods=['POST'])
def demotext():
    pic=request.get_json(force=True)
    imgData=preprocess(pic)
    
    print('got it!')
    return(str(ocr(imgData)))

@app.route('/gentext', methods=['POST'])
def gentext():
    word=request.get_json(force=True)
    print('got it!',word)
    return("1")
if __name__ == '__main__':
    app.run(debug=True,threaded=True)