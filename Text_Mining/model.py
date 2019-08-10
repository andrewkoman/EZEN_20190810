# 한글 사용 준비
from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
#정규표현식
import re

import nltk
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pylab as plt

class SamsungReport :
    def __init__(self):
        self.okt = Okt()


    def read_file(self):
        self.okt.pos("삼성전자 글로벌 센터 전자 사업부", stem=True)
        filename = "C:/Temp/pyCham/TF/20190803/Text_Mining/data/kr-Report_2018.txt"

        with open( filename, 'r', encoding='utf-8') as f:
            texts = f.read()

        return texts

    @staticmethod
    def extract_hangul(texts):
        temp = texts.replace('\n', ' ')
        # 한글만 추출
        tokenizer = re.compile(r'[^ ㄱ-힣]+')
        temp = tokenizer.sub('', temp)
        return temp

    @staticmethod
    def change_token(texts):
        tokens = word_tokenize(texts)
        print(tokens[:7])
        return tokens


    def extract_noun(self):
        #삼성전자의 스마트폰은  -> 삼성전자 스마트폰
        noun_token = []
        tokens = self.change_token(self.extract_hangul(self.read_file()))

        for token in tokens:
            token_pos = self.okt.pos(token)
            temp = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']

            if len(''.join(temp)) > 1 :
                noun_token.append("".join(temp))

        texts = " ".join(noun_token)
        print('==============추출된 명사======================')
        print(texts[:300])

        return texts

    # nltk 다운로드
    @staticmethod
    def download():
        nltk.download()

    # 필요 없는(분석 가치 없는) 단어 제거
    @staticmethod
    def read_stopword():

        stop_file = "C:/Temp/pyCham/TF/20190803/Text_Mining/data/stopwords.txt"

        with open( stop_file, 'r', encoding='utf-8') as f:
            stopwords = f.read()

        stopwords = stopwords.split(' ')
        print('--------제거 문자----------------')
        print(stopwords[:10])

        return stopwords

    def remove_stopword(self):
        texts = self.extract_noun()
        tokens = self.change_token(texts)
        stopwords = self.read_stopword()
        texts = [text for text in tokens if text not in stopwords]

        return texts


    def find_feqency(self):
        texts = self.remove_stopword()
        freqtxt = pd.Series( dict(FreqDist(texts))).sort_values(ascending=False)
        print(freqtxt[:30])

        return freqtxt

    def draw_wordcloud(self):
        #texts = self.find_feqency()
        texts = self.remove_stopword()

        wcloud = WordCloud('C:/Temp/pyCham/TF/20190803/Text_Mining/data/D2Coding.ttf', relative_scaling=0.2, background_color='white').generate(" ".join(texts))

        plt.figure(figsize=(12,12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
