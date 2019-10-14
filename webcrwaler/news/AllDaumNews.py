import  requests
from bs4 import  BeautifulSoup

#url = daum IT 전체기사
url = 'https://news.daum.net/breakingnews/digital'
resp = requests.get(url)
bs = BeautifulSoup(resp.text ,'html.parser') # 경고메세지를 없애기 위해서 html.parser ㅇ입력해줘야함

news_list  = bs.select('ul.list_news2 a.link_txt')

for news in news_list:
    news_url = news['href']
    doc = requests.get(news_url)
    soup = BeautifulSoup(doc.text, 'html.parser')
    print(news['href'])

    # 기사수집
    if len(soup.select('span.txt_info')) == 2:
        title = soup.select('h3.tit_view')[0].text.strip()
        reporter = soup.select('span.txt_info')[0].text.strip()
        reg_date = soup.select('span.txt_info')[1].text.strip()
        container = soup.select('div#harmonyContainer p')
        contents = ''
    else:
        if len(soup.select('span.txt_info')[0]) < 10:
            title = soup.select('h3.tit_view')[0].text.strip()
            reporter = '기자가 없다'
            reg_date = soup.select('span.txt_info')[0].text.strip()
            container = soup.select('div#harmonyContainer p')
            contents = ''
        else:
            title = soup.select('h3.tit_view')[0].text.strip()
            reporter = soup.select('span.txt_info')[0].text.strip()
            reg_date = '날짜가없다 ㅋ'
            container = soup.select('div#harmonyContainer p')
            contents = ''



    for p in soup.select('div#harmonyContainer p'):
        contents += p.text.strip()
    #기사 출력
    print('제목 : ', title)
    print('기자 : ', reporter)
    print('작성일자 : ', reg_date)
    print('내용 :', contents)

#print(news_list)