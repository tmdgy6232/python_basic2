# 가장 보통의연애 네이버 댓글
import requests
from bs4 import BeautifulSoup

#url 설정
count = 0 # 댓글 총 갯수
page = 1 # page 넘버
compare_reply = [] # 마지막 페이지를 찾기위한 댓글정보
while True:
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=182205&' \
          'type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(
        page)
    doc = requests.get(url)
    soup = BeautifulSoup(doc.text, 'html.parser')

    # 1페이지의 존재하는 댓글 10건 list
    reply_list = soup.select('div.score_result > ul > li')

    #댓글 10건 중 첫번째 댓글이 다음 페이지의 첫번째 댓글과
    #같으면 끝난 페이지임으로 break로 빠져나간다


    flag = reply_list[0].select('div.score_reple > p > span[id*="ment"]')[0].text
    if compare_reply ==  flag:
        break
    else:
        compare_reply = flag
        pass

    # 댓글 10건을 1건씩 꺼내서 reply에 담음
    for reply in reply_list:
         # 작성자 내용 평점 작성일자
         star_point = reply.select('div.star_score > em')[0].text
         writer = reply.select('div.score_reple > dl > dt > em')[0].text.strip()
         reg_date = reply.select('div.score_reple > dl > dt > em')[1].text.strip()
         content = reply.select('div.score_reple > p > span[id*="ment"]')[0].text
         total = reply.select('div.star_score')
         indexNo = writer.find('(')  # 초롱이(ch****)의 괄호를 삭제하기위해 (의 위치 탐색하는 코드
         indexYes = reg_date.find(' ')

         print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
         print('평점 : ', star_point)
         print('작성자 : ', writer[:indexNo])
         print('작성일자 : ', reg_date[:indexYes])
         print('내용 :', content)
         count += 1
    page += 1
print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
print('총', page,'페이지 , 데이터는', count, '건입니다.')
# print(reply_list)
# print(len(reply_list))
