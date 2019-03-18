from flask import Flask, render_template ,request,url_for
from data import articals
import base64
import json
import numpy as np
from img_process import preprocess
from MyChainList_gpu import ocr
from gen_text import gen_txt

app = Flask(__name__)
artic=articals()
gen_t=gen_txt()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/p5draw')
def p5draw():
    return render_template('p5draw.html')

@app.route('/sketch.js')
def sketch():
    return render_template('/sketch.js')

@app.route('/sketch_text.js')
def sketch_t():
    return render_template('/sketch_text.js')
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
@app.route('/demot', methods=['POST'])
def demot():
    txt=request.get_json()
    
    
    t={'txt':gen_t(txt['input'])}
    print(t)
    return json.dumps(t)

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=5000,threaded=True,debug=True)