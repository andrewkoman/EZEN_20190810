# 한글 사용 준비
from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import re

class SamsungReport :
    def __init__(self):
        pass

    @staticmethod
    def read_file(self):
        okt = Okt()
        okt.pos("삼성전자 글로벌 센터 전자 사업부", stem=True)
        filename = "./data/kr-Report_2018.txt"

        with open( filename, 'r', encoding='utf-8') as f:
            texts = f.read()

        return texts

    @staticmethod
    def extract_hangul(texts):
        temp = texts.replace('\n', ' ')
        tokenize = re.compile(r'[^ㄱ-힣]+')