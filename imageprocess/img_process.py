import base64
import numpy as np
from PIL import Image
def preprocess(jpgtxt):

        data = jpgtxt['imgURI'].split(',')[-1]
        data = base64.b64decode(data)
        #print(data.decode('UTF-8'))

        g = open("H:/Python Project/flask/temp.jpg",'wb')
        g.write(data)
        g.close()

        pic = Image.open("H:/Python Project/flask/temp.jpg")
        pic=pic.convert('L')
        pic=pic.resize((28,28))
        M = np.array(pic) #now we have image data in numpy
        threshold, upper, lower=150., 0., 1.0
        M=np.where(M>threshold, upper, lower)
        M=np.array([[M]],dtype=np.float32)
        return M
