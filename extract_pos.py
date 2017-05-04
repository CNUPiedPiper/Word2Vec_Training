# -*- coding: utf-8 -*-

from konlpy.tag import Twitter
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

twitter = Twitter()
f = open("test.txt", 'r')
corpus = codecs.open('output.txt', 'w', encoding='utf-8')

def flat(content):
    return ["{}/{}".format(word, tag) for word, tag in twitter.pos(content, norm=True, stem=True)]

''' Demo 
input_line = u'오늘 대전 날씨는 어때?'
output_list = twitter.pos(input_line, norm=True, stem=True)

for word, morp in output_list:
    print(word, morp)
'''

for line in f:
    corpus.write(' '.join(flat(unicode(line))) + '\n')

f.close()
