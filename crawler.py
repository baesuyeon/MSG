from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import time

driver = webdriver.Chrome('c:/informs/chromedriver.exe')
base_url = 'https://tv.naver.com/v/12286767/list/565077'

def get_data():
    video = driver.find_element_by_xpath('//*[@id="player"]/div/div/div[11]/div[13]/video')
    title = driver.find_element_by_xpath('//*[@id="clipInfoArea"]/div[1]/h3')
    views = driver.find_element_by_xpath('//*[@id="clipInfoArea"]/div[1]/div/span[1]')
    hash_list = driver.find_elements_by_css_selector('#clipInfoArea > div.hash_box > ul > li')
    time_info = driver.find_element_by_xpath('//*[@id="player"]/div/div[1]/div[11]/div[4]/div[3]/div[2]/div[1]/div[5]/span[3]/span')

    driver.implicitly_wait(30)  # seconds
    time.sleep(2)

    video_src = video.get_attribute('src')
    video_title = title.text
    video_views = views.text
    video_time = time_info.text
    video_hash = []

    # print(len(video_src))

    print(video_src)
    print(video_title)
    print(video_views)
    print(video_time)
    for h in hash_list:
        video_hash.append(h.text)
        print(h.text)

# 클립영상 저장 테스트
# url = 'https://naver-cjenm-c.smartmediarep.com/smc/naver/multi/eng/C01_293675/2f636a656e6d2f434c49502f45412f423132303139353833342f423132303139353833345f455049303030315f30315f7433352e6d7034/0-0-0/content.mp4?solexpire=1584451800&solpathlen=148&soltoken=5ae15951101d0edcbee3603e5a25426e&soltokenrule=c29sZXhwaXJlfHNvbHBhdGhsZW58c29sdXVpZA==&soluriver=2&soluuid=41f663db-0305-4e0e-b336-7d30a3387b39&itemtypeid=35&tid=rmcPlayer_15844086010118743'
# urllib.request.urlretrieve(url, 'c:/informs/video/test.mp4')

# nc = driver.find_element_by_xpath('//*[@id="playlistArea"]/div/div[1]/div[1]/strong/em')
# num_clip = nc.text.split('/')[1]
# print(num_clip)

driver.implicitly_wait(10) # seconds
driver.get('https://tv.naver.com/v/11789515/list/552637') # 사이트 접속
# driver.get('https://tv.naver.com/v/12419406') # 사이트 접속
time.sleep(5)

play_btn = driver.find_element_by_xpath('//*[@id="player"]/div/div[1]/div[8]') # play 버튼
if 'visible' in play_btn.get_attribute('style') :
    play_btn = driver.find_element_by_xpath('//*[@id="player"]/div/div[1]/div[8]/div/div/span/div/button[1]')
    play_btn.click()

time.sleep(7)

wait_txt = driver.find_element_by_xpath('//*[@id="player"]/div/div[1]/div[11]/div[9]/div[2]/span[2]')
if 'block' in wait_txt.get_attribute('style') : # WAIT 메세지가 있으면
    sec = driver.find_element_by_xpath('//*[@id="player"]/div/div[1]/div[11]/div[9]/div[2]/span[2]/p/em')
    time.sleep(int(sec.text) + 5)

skip_btn = driver.find_element_by_xpath('//*[@id="player"]/div/div[1]/div[11]/div[9]/div[2]/button')
if 'block' in skip_btn.get_attribute('style') : # SKIP 메세지가 있으면
    skip_btn.click()
    time.sleep(5)
    print("click!")

get_data()
