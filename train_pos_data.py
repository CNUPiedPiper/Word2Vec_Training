
# coding: utf-8

# In[8]:

import gensim
import codecs


# In[34]:

class SentenceReader:

    def __init__(self, filepath):
        self.filepath = filepath

    def __iter__(self):
        for line in codecs.open(self.filepath, encoding='utf-8'):
            yield line.split(' ')


# In[35]:

sentences_vocab = SentenceReader('/Users/jegalsumin/Documents/HARU/output.txt')
sentences_train = SentenceReader('/Users/jegalsumin/Documents/HARU/output.txt')

model = gensim.models.Word2Vec()
model.build_vocab(sentences_vocab)
model.train(sentences_train,total_examples=model.corpus_count,epochs=model.iter)


# In[38]:

model.most_similar(positive=["남자/Noun", "여왕/Noun"], negative=["여자/Noun"], topn=1)


# In[39]:

model.most_similar('날씨/Noun')


# In[65]:

model.most_similar(positive=['심상정/Noun','민주당/Noun'],negative=['문재인/Noun'],topn=1)


# In[64]:

model.vector_size


# In[ ]:



