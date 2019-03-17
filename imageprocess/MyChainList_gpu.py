import numpy as np
import chainer
from chainer.backends import cuda
from chainer import Function, gradient_check, report, training, utils, Variable
from chainer import datasets, iterators, optimizers, serializers
from chainer import Link, Chain, ChainList
import chainer.functions as F
import chainer.links as L
from chainer.training import extensions
import os

# Network definition
class MLP(ChainList):

    def __init__(self, conv_layer=[],fully_connect_layer=[10,2]):
        super(MLP, self).__init__()
        self.n1 = len(conv_layer)
        self.n2 = len(fully_connect_layer)
        with self.init_scope():
            for n in conv_layer:
                self.add_link(L.Convolution2D(None, out_channels=n,ksize=(3,3),stride=1))
            for n in fully_connect_layer:
                self.add_link(L.Linear(None,n))

    def __call__(self, x):
        out=x
        for i1 in range(self.n1):
            out = F.relu(self[i1](out))
            out = F.max_pooling_2d(out,2)
        for i2 in range(self.n2):
            out = F.relu(self[i1+1+i2](out))
        return out

def ocr(data):
    file_name='H:/Python Project/flask/imageprocess/Model_gpu_C16_f30_20_10'
    #file_name='snapshot_iter_7200'
    #load the classifier
    model=MLP(conv_layer=[16],fully_connect_layer=[30,20,10])
    chainer.serializers.load_npz(file_name,model)
    data=model(data).data
    print(data)
    return(np.argmax(data))

