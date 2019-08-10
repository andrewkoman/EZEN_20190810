from webcrawl.assembly import AssemblyCrawler
from webcrawl.bugsmusic import BugsCrawler
from webcrawl.krx import KrxCrawler
from webcrawl.naver_stock import StockModel
from webcrawl.naver_movie import NaverMoive
from webcrawl.naver_login import NaverLogin

class WebCrawlController :
    def __init__(self):
        pass


    def exec(self, flag):
        if flag == 'a' :
            a= AssemblyCrawler("http://likms.assembly.go.kr/bill/billDetail.do?billId=PRC_R1N9J0N1X0Y9A1O8S3R5Z3J3K9O8N7")
            a.scrap()
        elif flag == 'b' :
            b = BugsCrawler('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20190810&charthour=11')
            b.scap()
        elif flag == 'k' :
            k = KrxCrawler("https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo")
            k.scarp()
        elif flag == 'ns' :
            ns = StockModel('005930')
            ns.scarp()
        elif flag == 'nm' :
            nm = NaverMoive('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
            nm.scap()
        elif flag == 'nl' :
            nl = NaverLogin('https://nid.naver.com/nidlogin.login')
            nl.auto_login()


# https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo