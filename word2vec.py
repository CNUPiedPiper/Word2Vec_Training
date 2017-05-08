# coding: utf-8

import gensim
import codecs

model = gensim.models.Word2Vec.load('/Users/jegalsumin/Documents/Word2Vec_Training/model')

def get_word2vec(word):
    return model.wv[word]


