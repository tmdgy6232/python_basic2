import requests
from bs4 import BeautifulSoup
from selenium import webdriver

doc = requests.get('https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx')
print(doc.text)

#크롬 드라이버 접속 및 경로설정
path = 'E:\Bigdata\webdriver\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)

#url 설정
driver.get('https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx')

#에러제거
#soup = BeautifulSoup(driver.page_source, 'html.parser')


search = driver.find_element_by_id('cphContents_cphContents_cphContents_ddlSeries_ddlSeries')

select = driver.find_element_by_xpath("//select[@id='cphContents_cphContents_cphContents_ddlSeries_ddlSeries']/option[@value='0']").click()

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.implicitly_wait(3)
doc = requests.get(driver.page_source)
#print(doc.text)
docf = driver.page_source
print(docf.text)
#_data = soup.select('tbody > tr')[0].text.strip()
#print(_data)
