#다음 뉴스 1건 출력(제목, 기자, 작성일자, 내용)

import requests
from bs4 import BeautifulSoup

#url 설정
url = 'https://sports.v.daum.net/v/20191002102202891'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')

# 수집
title = soup.select('h3.tit_view')[0].text.strip()
reporter = soup.select('span.txt_info')[0].text.strip()[:3]
reg_date = soup.select('span.txt_info')[1].text.strip()[3:13]
container = soup.select('div#harmonyContainer p')
contents = ''

for p in container:
    contents += p.text.strip()


#출력
print('제목 : ', title)
print('기자 : ', reporter)
print('작성일자 : ', reg_date)
print('내용 :' , contents)


