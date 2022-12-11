import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import statistics
from statistics import mode

def sen(inputs):
    LRmodel = pickle.load(open('C:/Users/nalia-pc/Dropbox/PC/Documents/===KULIAH===/Kuliah Semester 5/NLP/Ujian/UAS/KomSight/models/LRmodel.pkl','rb'))
    SVCmodel = pickle.load(open('C:/Users/nalia-pc/Dropbox/PC/Documents/===KULIAH===/Kuliah Semester 5/NLP/Ujian/UAS/KomSight/models/SVCmodel.pkl','rb'))
    BNBmodel = pickle.load(open('C:/Users/nalia-pc/Dropbox/PC/Documents/===KULIAH===/Kuliah Semester 5/NLP/Ujian/UAS/KomSight/models/BNBmodel.pkl','rb'))
    tfidf = pickle.load(open('C:/Users/nalia-pc/Dropbox/PC/Documents/===KULIAH===/Kuliah Semester 5/NLP/Ujian/UAS/KomSight/models/tfidf.pkl','rb'))

    # inputs = """"""
    # # tfidf = TfidfVectorizer(ngram_range=(1,1))

    # tfidf.fit_transform([inputs])
    X_test = tfidf.transform([inputs])

    all_sen = (LRmodel.predict(X_test)[0], SVCmodel.predict(X_test)[0], BNBmodel.predict(X_test)[0])
    # print(all_sen)
    
    def most_common(List):
        return(mode(List))

    return(most_common(all_sen))