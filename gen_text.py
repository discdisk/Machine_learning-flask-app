#!/usr/bin/env python
"""Sample script of recurrent neural network language model.
This code is ported from the following implementation written in Torch.
https://github.com/tomsercu/lstm
"""
from __future__ import division
import argparse

import numpy as np

import chainer
import chainer.functions as F
import chainer.links as L
from chainer import training
from chainer.training import extensions
import pickle

# Definition of a recurrent net for language modeling
class RNNForLM(chainer.Chain):

    def __init__(self, n_vocab, n_units):
        super(RNNForLM, self).__init__()
        with self.init_scope():
            self.embed = L.EmbedID(n_vocab, n_units)
            self.l1 = L.LSTM(n_units, n_units)
            self.l2 = L.LSTM(n_units, n_units)
            self.l3 = L.Linear(n_units, n_vocab)

        for param in self.params():
            param.data[...] = np.random.uniform(-0.1, 0.1, param.data.shape)

    def reset_state(self):
        self.l1.reset_state()
        self.l2.reset_state()

    def __call__(self, x):
        h0 = self.embed(x)
        h1 = self.l1(F.dropout(h0))
        h2 = self.l2(F.dropout(h1))
        y = self.l3(F.dropout(h2))
        return y


class gen_txt(object):
    """docstring for gen_txt"""
    def __init__(self):
        super(gen_txt, self).__init__()

        rnn = RNNForLM(7604, 650)
        model = L.Classifier(rnn)
        chainer.serializers.load_npz('model_true.npz', model)
        model.predictor.reset_state()
        self.model=model
        self.dictionary=pickle.load(open('one_hot_data.txt','rb'))
        self.dictionary_out={i:j for i , j in enumerate(self.dictionary)}


    def __call__(self,input_d,length=1000):
        out=input_d
        for x in range(length):
            answer=self.model.predictor(np.array([self.dictionary[input_d]]))
            answer=F.softmax(answer)
            
            input_d=self.dictionary_out[np.argmax(answer.data)]

            if input_d == '\n':
                out+='<br>'
            else:
                out+=input_d
        return(out)


def main():



    # Prepare an RNNLM model
    rnn = RNNForLM(7604, 650)
    model = L.Classifier(rnn)



    chainer.serializers.load_npz('model_true.npz', model)



    model.predictor.reset_state()


    dictionary=pickle.load(open('one_hot_data.txt','rb'))
    dictionary_out={i:j for i , j in enumerate(dictionary)}

    input_d='自然'
    out='自然'
    for x in range(1000):
        answer=model.predictor(np.array([dictionary[input_d]]))
        answer=F.softmax(answer)
        
        input_d=dictionary_out[np.argmax(answer.data)]
        out+=input_d
    print(out)


if __name__ == '__main__':
    main()