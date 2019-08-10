from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsCrawler :
    def __init__(self, url) :
        print('aaaaaaaaaaaa')
        self.url = url


    def scap(self):
        print('bbbbbbb')
        soap = BeautifulSoup(urlopen(self.url), "html.parser")
        n_artist = 0
        n_title = 0
        for i in soap.find_all(name='p' , attrs=( {'class':'artist'}) ):
            n_artist += 1
            print(str(n_artist) + '위')
            print('아티스트:' + i.find('a').text)
            print('------------------')

        for i in soap.find_all(name='p' , attrs=( {'class':'artist'}) ):
             n_title += 1
             print(str(n_title) + '위')
             print('음악:' + i.find('a').text)
             print('------------------')