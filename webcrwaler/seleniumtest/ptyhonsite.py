#pythonsite
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# selenium driver()의 매서드()
# 1. URL에 접근하는 API
# get('https://python.org)

# 2.page의 단일 dlement에 접근하는 api
# - find_element_by_name('HTML_name')
# - find_element_by_id('HTML_id')
# - find_element_by_xpath('/html/body/some/xpath')

# 3. page의 여러 element에 접근하는 api
# - find_element_by_css_selector('#css > div.selector')
# = find_element_by_class_name('some_class_name')
# - find_element_by_tag_name('h1')
# 2, 3번 매서드를 사용히 html을 브라우저에서 파싱하기 때문에
# python과 BeatifulSoup를 사용하지 않아도 된다.
# but, selenium built in 함수만 사용하면 불편하기 때문에
# Beautifulsoup 객체를 이용하면 driver.page.source API를
# 사용하여 현재 랜더링 된 페이지의 elements를 모두 가져올 수 있다.

# chrome driver가 위치하는 주소
path = 'E:\Bigdata\webdriver\chromedriver_win32\chromedriver.exe'

#chrome webdriver 생성
driver = webdriver.Chrome(path)

#chrome 드라이버로 접속할 url
driver.get('https://www.python.org') # 핵심 : https://까지 꼭 적을것

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려준다.
driver.implicitly_wait(3)

#셀레니움은 클래스는 복수선택자이기 때문에, 아이디 또는 네임값만 받을 수 있다.
#웹 드라이버에서 아이디가 id-search-field인 태그를 찾아라
#id가 id-search-field인 태그를 찾아서 search 변수에 담음
search = driver.find_element_by_id('id-search-field')

#input 태그 값 초기화
search.clear()

#input 태그에 'lambda'값을 입력
search.send_keys('lambda')

#검색버튼 click()
search.send_keys(Keys.RETURN)