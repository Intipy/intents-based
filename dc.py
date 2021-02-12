import requests
from bs4 import BeautifulSoup
import random
import time
import urllib
import lxml       
from selenium import webdriver
import os

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0")
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)



headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'    #GET을 할때의 헤더값 / user-agent만 지정
}


while 1 < 2:
    try:
        print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
        print('ㅡㅡㅡㅡㅡ크롤링 중ㅡㅡㅡㅡㅡ')
        print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
        time.sleep(20)

        kk = random.randint(1, 16715404)                                                                 
        url = 'https://gall.dcinside.com/mgallery/board/view/?id=aoegame&no='+str(kk)+'&page=1'
        res = requests.get(url, headers=headers)

        while res.status_code != 200:
            kk = random.randint(1, 16715403)
            url = 'https://gall.dcinside.com/mgallery/board/view/?id=aoegame&no='+str(kk)+'&page=1'                
            res = requests.get(url, headers=headers)                                                      #중갤로부터 게시물 랜덤 선택 후 GET


        soup = BeautifulSoup(res.text, 'lxml')
        title = soup.find('span', attrs = {'class':'title_subject'})
        des = soup.find('div', attrs = {'class':'writing_view_box'})
        t = title.get_text()
        d = des.get_text() + '.'     #중갤 게시물로부터 제목과 내용을 크롤링
        print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
        print('ㅡㅡㅡㅡㅡ크롤링 완료ㅡㅡㅡㅡㅡ')
        print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')



        print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
        print('ㅡㅡㅡㅡㅡ게시물 작성 중ㅡㅡㅡㅡㅡ')
        print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
        driver = webdriver.Chrome(options=options) #크롬버젼과 맞는걸로
        driver.get("https://gall.dcinside.com/mini/board/lists/?id=jaemmin") #갤러리 글쓰기 주소
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/section[1]/article[2]/div[1]/div[3]/div/div[2]/a").click()
        driver.find_element_by_name('name').send_keys('ㅇㅇ')#닉네임
        driver.implicitly_wait(1)
        time.sleep(random.uniform(1,3))
 
        driver.find_element_by_name('password').send_keys('12357890')#비밀번호
        driver.implicitly_wait(1)
        time.sleep(random.uniform(1,3))
 
        driver.find_element_by_name('subject').send_keys(t)
        # HTML으로 쓰기 방식 변경
        driver.find_element_by_id("chk_html").click();
        time.sleep(1)

        # 글쓰기 폼으로 진입
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@name='tx_canvas_wysiwyg']"))
        print(driver.page_source)

        #본문 입력
        time.sleep(1)
        driver.find_element_by_tag_name("body").send_keys(d)
        time.sleep(1)

        driver.switch_to_default_content()
        #글쓰기 저장
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[2]/main/section/article[2]/form/div[5]/button[2]").click()
        #저장 딜레이
        time.sleep(2)
        print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
        print('ㅡㅡㅡㅡㅡ게시물 작성 완료ㅡㅡㅡㅡㅡ')
        print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
        #웹페이지 닫기
        time.sleep(1)
        driver.close()

    except:
        pass
