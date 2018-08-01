#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: vysh
"""

from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from string import punctuation

f=open('extracted.txt')
text=f.read()
not_words = []
words=word_tokenize(text)
for word in words:
    if not wordnet.synsets(word.lower()):
         not_words.append(word)
         
filtered = [w for w in not_words if not w in stopwords.words('english') + list(punctuation)]

print(filtered)
