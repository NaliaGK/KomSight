import numpy as np
from flask import Flask, request, render_template
import pickle
import News_retriever
import sentiment
import WordCloud
import Summary
#objective
app = Flask(__name__)

#home route
@app.route('/', methods=['POST', 'GET'])
def home(): 
    return render_template('index.html')

#predict route
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    artikel = ''
    judul = ''
    sentimen_result = ''
    summary = ''
    if request.method == 'POST':
        artikel, judul = News_retriever.getter(request.form['link kompas'])
        sentimen_result = sentiment.sen(artikel)
        WordCloud.wordcloud(artikel, sentimen_result)
        summary = Summary.print_summary(artikel)
    else:
        artikel = 'pls wait a sec and click submit again'    
    return render_template('predict.html', artikel=artikel, judul=judul, sentimen_result=sentimen_result, summary=summary)




if __name__ == "__main__":
    app.run()