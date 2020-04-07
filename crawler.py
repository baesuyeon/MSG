from selenium import webdriver
import urllib.request
import time

from selenium.webdriver.common.keys import Keys

import datas
import re

driver = webdriver.Chrome('c:/informs/chromedriver.exe')

def calculate_time(str) :
    if '분' in str:
        if '초' in str:
            s = str.split('분')
            minute = int(re.findall('\d+', s[0])[0])
            sec = int(re.findall('\d+', s[1])[0])
            time = minute * 60 + sec
        else :
            minute = int(re.findall('\d+', str)[0])
            time = minute * 60
    else:
        sec = int(re.findall('\d+', str)[0])
        time = sec
    return time

def get_base_url(search_word):
    list_str = search_word.split()
    last_word = list_str[-1]
    episode = int(re.findall('\d+', last_word)[0])

    print('episode: ' + str(episode))
    name = str()
    print(list_str)
    for i in range(0, len(list_str) - 1):
        name += list_str[i]
    print(name)

    driver.get('https://tv.naver.com/')
    search = driver.find_element_by_xpath('//*[@id="searchQuery"]')
    # search 변수에 저장된 곳에 값을 전송
    search.send_keys(name)
    time.sleep(1)
    # search 변수에 저장된 곳에 엔터를 입력
    search.send_keys(Keys.ENTER)
    search = driver.find_element_by_xpath('//*[@id="channel_list"]/li[1]/div/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="nav"]/ul/li[2]/a').click()
    time.sleep(1)

    body = driver.find_element_by_tag_name('body')
    num_of_pagedowns = 50
    while num_of_pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)
        num_of_pagedowns -= 1
        try:
            driver.find_element_by_xpath('//*[@id="cds_flick"]/div/div[2]/div/div/div/div/div[3]/a').click()
        except:
            None

    search = name + ' ' + str(episode)
    print('search : ' + search)

    i = 1
    # print('i' + str(i))
    while True:
        s = '//*[@id="cds_flick"]/div/div[2]/div/div/div/div/div[2]/div[' + str(i) + ']'
        try :
            check = driver.find_element_by_xpath(s)
        except:
            break
        title = driver.find_element_by_xpath(s + '/h3').text
        # print('title: ' + title)

        list_title = title.split()
        last = list_title[-1]
        extract = int(re.findall('\d+', last)[0])

        if episode == extract:
            url = driver.find_element_by_xpath(s + '/h3/a').get_attribute('href')
            return url, episode
        i += 1

def get_data(num, Clips, episode):
    test_clip = datas.Clip()
    test_hash = datas.Hash()

    video = driver.find_element_by_xpath('//*[@id="player"]/div/div/div[11]/div[13]/video')
    title = driver.find_element_by_xpath('//*[@id="clipInfoArea"]/div[1]/h3')
    views = driver.find_element_by_xpath('//*[@id="clipInfoArea"]/div[1]/div/span[1]')
    hash_list = driver.find_elements_by_css_selector('#clipInfoArea > div.hash_box > ul > li')
    vod = driver.find_element_by_xpath('//*[@id="topChannelInfo"]/div/div[1]/h2/a')

    driver.implicitly_wait(30)  # seconds
    time.sleep(2)

    time_info = driver.find_element_by_xpath('//*[@id="player"]/div/div[1]/div[11]/div[4]/div[3]/div[2]/div[1]/div[5]/span[3]/span')

    vod_name = vod.text
    video_src = video.get_attribute('src')
    video_title = title.text
    video_views = views.text
    video_time = time_info.get_attribute('aria-label')
    video_hash = []

    if '예고' in video_title:
        return

    if '메이킹' in video_title:
        return

    # print(len(video_src))
    if 'blob' in video_src:
        video = driver.find_element_by_xpath('//*[@id="player"]/div/div[1]/div[11]/div[13]/video/source')
        url = video.get_attribute('src')
        test_clip.add_clip('url')
        print(url)
    else:
        url = video_src
        urllib.request.urlretrieve(url, 'c:/informs/video/' + vod_name + '_' + str(episode) + '화' + '_clip' + str(num) + '.mp4') # 클립 영상이 저장되는 경로

    print(video_src)
    test_clip.add_clip(video_src)  # 클립 경로
    print(video_title)
    test_clip.add_title(video_title)  # 클립 제목
    print(video_views)
    test_clip.add_views(video_views)  # 클립 조회수
    print(video_time)
    test_clip.add_time(calculate_time(video_time))  # 클립 시간
    for h in hash_list:
        video_hash.append(h.text)  # 클립 해시
        print(h.text)
        test_hash.add_hash(h.text)
    test_clip.add_clip('c:/informs/video/clip' + vod_name + '_' + str(episode) + '화' + '_clip' + str(num))

    clip = []
    clip.append(test_clip)
    clip.append(test_hash)
    Clips.append(clip)


    print('-------------------------------------------------------')

def crawler(Clips, search_word, vod_no) :
    base_url, episode = get_base_url(search_word)
    driver.get(base_url)
    nc = driver.find_element_by_xpath('//*[@id="playlistArea"]/div/div[1]/div[1]/strong/em')
    num_clip = int(nc.text.split('/')[1])
    print('Total Clip : ' + str(num_clip))

    for i in range(1, num_clip + 1) :
        # print('Clip' + str(i))
        if i == 1 :
            card = driver.find_element_by_xpath('//*[@id="playlistClip"]/li[' + str(i) + ']/div[2]/a').get_attribute('href')
        else :
            card = driver.find_element_by_xpath('//*[@id="playlistClip"]/li[' + str(i) + ']/div/a').get_attribute('href')

        driver.implicitly_wait(10) # seconds
        driver.get(card)
        # driver.get('https://tv.naver.com/v/11789515/list/552637') # 사이트 접속
        # driver.get('https://tv.naver.com/v/12419406') # 사이트 접속
        time.sleep(5)

        play_btn = driver.find_element_by_xpath('//*[@id="player"]/div/div[1]/div[8]') # play 버튼
        if 'visible' in play_btn.get_attribute('style') :
            play_btn = driver.find_element_by_xpath('//*[@id="player"]/div/div[1]/div[8]/div/div/span/div/button[1]')
            play_btn.click()

        time.sleep(7)

        wait_txt = driver.find_element_by_xpath('//*[@id="player"]/div/div[1]/div[11]/div[9]/div[2]/span[2]')
        if 'block' in wait_txt.get_attribute('style') : # WAIT 메세지가 있으면
            # sec = driver.find_element_by_xpath('//*[@id="player"]/div/div[1]/div[11]/div[9]/div[2]/span[2]/p/em')
            time.sleep(5)

        skip_btn = driver.find_element_by_xpath('//*[@id="player"]/div/div[1]/div[11]/div[9]/div[2]/button')
        if 'block' in skip_btn.get_attribute('style') : # SKIP 메세지가 있으면
            skip_btn.click()
            time.sleep(5)
            print("click")

        get_data(i, Clips, episode)

# 클립영상 저장 테스트
# url = 'https://naver-cjenm-c.smartmediarep.com/smc/naver/multi/eng/C01_293675/2f636a656e6d2f434c49502f45412f423132303139353833342f423132303139353833345f455049303030315f30315f7433352e6d7034/0-0-0/content.mp4?solexpire=1584451800&solpathlen=148&soltoken=5ae15951101d0edcbee3603e5a25426e&soltokenrule=c29sZXhwaXJlfHNvbHBhdGhsZW58c29sdXVpZA==&soluriver=2&soluuid=41f663db-0305-4e0e-b336-7d30a3387b39&itemtypeid=35&tid=rmcPlayer_15844086010118743'
# urllib.request.urlretrieve(url, 'c:/informs/video/test.mp4')