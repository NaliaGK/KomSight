import numpy as np
from flask import Flask, request, render_template
import pickle
import News_retriever
import sentiment
import Summary
import webbrowser
from threading import Timer
import WordCloud
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

        WordCloud.wordcloud(str(artikel), str(sentimen_result))
        summary = Summary.print_summary(artikel)
    else:
        artikel = 'pls wait a sec and click submit again'    
    return render_template('predict.html', artikel=artikel, judul=judul, sentimen_result=sentimen_result, summary=summary)

def open_browser():
      webbrowser.open_new("http://127.0.0.1:2000")

if __name__ == "__main__":
      Timer(1, open_browser).start()
      app.run(port=2000)