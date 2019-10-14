import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from pymongo import MongoClient

#2019.10.07 bu seunghyo
#desc : Selenium과 BeautifulSoup를 사용하여
#       다음 영화평 수집(댓글, 작성자, 평점, 작성일자)
#       수집된 데이터를 몽고db에 저장하는 프로그램

# selenium 설정
path = 'E:\Bigdata\webdriver\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)

#MongoDB Connection
client = MongoClient('localhost', 27017) # 클래스 객체 할당 (ip주소, port번호)
#mongoDB에 계정이있거나 외부ip인 경우
# DB_HOST = 'xxx.xx.xx.xxx:27017'
# DB_ID = 'root'
# DB_PW = 'pw'
# client = MongoClient('mongodb://%s:%s@%s' % (DB_ID, DB_PW, DB_HOST)

#mongoDB의 local DB를 할당해준것
db = client['local']
collection = db.movie


def mongo_write(data):
    print('>>> MongoDB write data!')
    collection.insert(data)  # JSON 타입의 데이터를 넣어야함 = dict Type(python)


#url 설정
#웹 크롤링
def crawler(code):
    count = 0  # 댓글 총 갯수
    page = 0  # page 넘버

    while True:
        page += 1
        url = 'https://movie.daum.net/moviedb/grade?movieId={}&type=netizen&page={}'.format(code, page)
        driver.get(url)  # http://까지 적어야함
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        reply_list = soup.select('ul.list_review > li')
        if reply_list == []:  # 다음 페이지에 아무것도 뜨지 않으면, 브레이크해라
            page = page - 1
            break
        else:
            pass
        for reply in reply_list:
            content = reply.select('p.desc_review')[0].text.strip()
            writer = reply.select('div > a > em.link_profile')[0].text.strip()
            score = reply.select('div em.emph_grade')[0].text.strip()
            reg_date = reply.select('div span.info_append')[0].text.strip()
            indexNo = reg_date.find(',')
            reg_date = reg_date[:indexNo]

            #mongoDB에 댓글 저장
            data = {
                    'score': score,
                    'writer': writer,
                    'reg_date': reg_date,
                    'content': content}

            mongo_write(data)


            print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
            print('평점 : ', score)
            print('작성자 : ', writer)
            print('작성일자 : ', reg_date)
            print('내용 : ', content)
            count += 1
    print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
    print('총 ', page, '페이지, 데이터는 ', count, '건 출력되었습니다.')


#실행부
crawler(127878)


