from webcrawl.controller import WebCrawlController


if __name__ == '__main__':
    print('a. 국회 크롤링  ')
    print('b. 벅스 크롤링  ')
    print('k. 증권 크롤링  ')
    print('ns. 네이터 주가 조회')
    print('nm. 네이터 영화 조회')
    print('nl. 네이터 로그인')
    print('0. 종료  ')
    crawl = WebCrawlController()

    flag = input('크롤링 선택\n')
    result = crawl.exec(flag)
    print("수행결과 : %s" % result)
