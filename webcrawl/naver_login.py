#from bs4 import BeautifulSoup
from selenium import webdriver
from bs4 import BeautifulSoup

class NaverLogin :
    def __init__(self, url):
        self.driver = webdriver.Chrome(
        executable_path='C:/Temp/pyCham/TF/20190803/webcrawl/data/chromedriver_76.0.3809.68')
        self.driver.implicitly_wait(3)
        self.driver.get(url)
        #self.soup = BeautifulSoup(driver.page_source, 'html.parser')

    def auto_login(self):
        self.driver.find_element_by_name('id').send_keys('******')
        self.driver.find_element_by_name('pw').send_keys('******')

        self.driver.implicitly_wait(3)

        self.find_element_by_xpath('//*[@id=frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(3)

        self.driver.get('https://order.pay.naver.com/home')
        html = self.driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        notice = soup.select('div.p_inr > div.p_info > a > span')

        for i in notice :
            print(i.text.strip())