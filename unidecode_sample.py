#coding: utf-8
import unidecode
import sys
import codecs

sys.stdin = codecs.getreader('utf-8')(sys.stdin)

#change umlaut to un-umlaut alphabet
for line in sys.stdin:
  line=line.rstrip()
  print unidecode.unidecode(line)
