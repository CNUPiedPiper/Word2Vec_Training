
# coding: utf-8

import gensim
import codecs


class SentenceReader:

    def __init__(self, filepath):
        self.filepath = filepath

    def __iter__(self):
        for line in codecs.open(self.filepath, encoding='utf-8'):
            yield line.split(' ')


#sentences_vocab = SentenceReader('/Users/jegalsumin/Documents/HARU/output.txt')
#sentences_train = SentenceReader('/Users/jegalsumin/Documents/HARU/output.txt')

sentences_vocab = SentenceReader('# Your specific path of output file')
sentences_train = SentenceReader('# Your specific path of output file')

model = gensim.models.Word2Vec()
model.build_vocab(sentences_vocab)
model.train(sentences_train,total_examples=model.corpus_count,epochs=model.iter)

''' Demo
print(model.most_similar(positive=["남자/Noun", "여왕/Noun"], negative=["여자/Noun"], topn=1))

print(model.most_similar('날씨/Noun'))

print(model.most_similar(positive=['심상정/Noun','민주당/Noun'],negative=['문재인/Noun'],topn=1))
'''
