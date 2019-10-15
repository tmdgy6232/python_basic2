import requests
from bs4 import BeautifulSoup
from selenium import webdriver

doc = requests.get('https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx')


#크롬 드라이버 접속 및 경로설정
path = 'E:\Bigdata\webdriver\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)

#url 설정
driver.get('https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx')
driver.implicitly_wait(3)
#에러제거


search = driver.find_element_by_id('cphContents_cphContents_cphContents_ddlSeries_ddlSeries')

select = driver.find_element_by_xpath("//select[@id='cphContents_cphContents_cphContents_ddlSeries_ddlSeries']/option[@value='0']").click()

soup = BeautifulSoup(driver.page_source, 'html.parser')
_datatotal = driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_udpContent"]/div[3]/table/tbody/tr')
_data2 = driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_udpContent"]/div[3]/table/tbody/tr[2]')

for i in _datatotal:
    _data = driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_udpContent"]/div[3]/table/tbody/tr[i]').text
    print(_data)
_data_list = _data.split(' ')
print(_data_list)
print(_data_list[1])
print(_datatotal.text)
print(type(_data))
print(_data2.text)
