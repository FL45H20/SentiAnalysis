#future for converting python2 to python3
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

#import textblob for sentimnet analysis
from textblob import TextBlob

#for passing text as cmdline arg
import sys

#get user i/p for para to analyze
#get sentiment for each cmd line arg
for i in range(len(sys.argv) -1):
  para = sys.argv[i+1]
  print (para)

  #create a TextBlob object
  para =  TextBlob(para)

  #get sentinent
  #Polarity is float which lies in the range of [-1,1] where 1 means positive
  #Subjectivity is float liew beween [0,1] where 1 means personal opinion, emotion or judgment whereas 0 means objective which is factual infor>
  print ("Polarity: " + str(para.sentiment.polarity) + " Subjectivity: " + str(para.sentiment.subjectivity))
