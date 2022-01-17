"""Preprocess text file for language model training."""
from __future__ import print_function, division
import codecs
import re
filepath='war_and_peac.txt'
out_file='wap.txt'
# Regexes used to clean up the text
NEW_LINE_IN_PARAGRAPH_REGEX = re.compile(r'(\S)\n(\S)')
MULTIPLE_NEWLINES_REGEX = re.compile(r'(\n)(\n)+')

#we will read text as string
with codecs.open(filepath,encoding='utf-8',mode='r') as fi:
    book=fi.read()

#cleaning
"""we will strip out newlines in the middle of sentences and reduce the maximum number of 
consecutive newlines allowed to two"""
book= NEW_LINE_IN_PARAGRAPH_REGEX.sub('\g<1> \g<2>', book)
book=MULTIPLE_NEWLINES_REGEX.sub('\n\n',book)
book = re.sub(u'[\u201c\u201d]', '"', book)

# Write proccessed text to file
with codecs.open(out_file, encoding='utf-8', mode='w')as f_output:
    f_output.write(book)