import stylecloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import string
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# teks = 'Hari ini aku ke sana'
# sentimen = 'NEGATIF'
def wordcloud(inputs, sen):
    teks = inputs
    
    list_stopwords = stopwords.words('indonesian') #stopwords
    newStopWords = ['yang','dengan', 'dan', 'juga']
    list_stopwords.extend(newStopWords)

    word_tokens = word_tokenize(teks) #tokening
   
    clean = [w for w in word_tokens if not w.lower() in list_stopwords]
  
    clean = []
  
    for w in word_tokens:
        if w not in list_stopwords:
            clean.append(w)

    clean = ' '.join(clean)

    clean =  re.sub(r'\w*\d+\w*', '', clean)
    clean =  re.sub('[%s]' % re.escape(string.punctuation), '', clean)

    if sen == "POSITIF":
        color = 'cmocean.diverging.Delta_20'
    else:
        color = 'cmocean.diverging.Balance_20'

    stylecloud.gen_stylecloud(clean,
                          icon_name='fas fa-cloud',
                          palette=color,
                          output_name='.\static\img\wordcloud.png',
                          collocations=False)

# wordcloud(teks, sentimen)