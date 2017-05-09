# Word2Vec_Training

## Dependency
```
$ easy_install -U gensim

$ sudo apt-get install python-dev
$ sudo pip install konlpy
```
## Word2Vec training from Namu-wiki data using KoNLPy & Gensim

1. Cleansing namu_wiki json file to only korean text file.
2. Extracting POS(Part-Of-Speech) from setences using KoNLPy.
3. Training Word2Vec from cleaned pos data.
