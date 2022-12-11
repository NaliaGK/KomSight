import stylecloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import string
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# teks = 'Jenis bom yang digunakan oleh terduga pelaku Agus Sujatno alias Agus Muslim di Polsek Astanaanyar, Bandung, Jawa Barat, merupakan bom panci. Ledakan bom membuat sebagian bangunan di Polsek Astanaanyar rusak. Selain itu satu anggota polisi gugur dan beberapa alami luka-luka. "Terkait dengan bom yang digunakan oleh pelaku adalah jenis bom panci," kata Karo Penmas Divisi Humas Polri Brigjen Pol Ahmad Ramadhan di Polrestabes Bandung, Kamis (8/12/2022). "Daya ledaknya mengakibatkan sebagian bangunan kantor Polsek Astana Anyar mengalami kerusakan," jelasnya. Isi bom panci Dilansir dari Antara, Komandan Satbrimob Polda Jawa Barat Kombes Pol. Yuri Karsono menjelaskan, dari hasil olah TKP, bom panci yang dibawa pelaku berisi proyektil paku. Selain itu, ditemukan pula residu triaceton triperoxide (TATP) dan baterai yang diduga digunakan sebagai pemantik bom. "Jenis bom yang meledak adalah jenis bom rakitan, dirakit dalam bentuk panci, dan biasa rekan-rekan dengar dengan bom panci," kata Yuri dalam konferensi pers di Polrestabes Bandung, Kota Bandung Jawa Barat, Kamis. Sementara itu, soal daya ledak bom tersebut, Yuri mengaku masih melakukan pendalaman dengan Tim Penjinak Bom dan Pusat Laboratorium Forensik. Buru kelompok di balik teror bom Bandung Dilansir dari Antara, Kepala Badan Nasional Penanggulangan Terorisme (BNPT) Komjen Pol. Boy Rafli Amar di Bandung, menegaskan, pihaknya menyelidiki kelompok-kelompok yang diduga memberi bantuan terhadap aksi AS. Saat ini BNPT tengah berkoordinasi dengan pihak-pihak tertentu untuk mengungkap jaringan AS. "Kami masih ingin terus mencoba melihat kelompok lain yang memberikan perbantuan, kami terus menyelidiki ke arah itu," kata Boy saat meninjau Polsek Astanaanyar, Kota Bandung, Jawa Barat, Kamis.'
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