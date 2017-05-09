import ijson
import io
import re

f = open('namuwiki_161031.json', 'r')
objects = ijson.items(f, 'item.text')

with io.open('test.txt', 'w', encoding='utf-8') as fw:
    split_word = " . ".split()
    i = 1
    for item in objects:
        if i == 100000: # until 100,000 pages
            break
        for s in split_word:
            item = item.replace(s,u'u000a')
        #item = ''.join([w for w in item if not (w.isdigit() or re.match(r'[A-Z]+', w, re.I))])

        # Extract only Korean
        item =  ''.join(re.findall(u'[\u000a\u0020\u050c\u3131-\u3163\uac00-\ud7a3]+', item))

        #print(item)
        fw.writelines(item)
        i = i+1
