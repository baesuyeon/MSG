from selenium import webdriver
import urllib.request

driver = webdriver.Chrome('c:/informs/chromedriver.exe')

# 클립영상 저장 테스트
# url = 'https://naver-cjenm-c.smartmediarep.com/smc/naver/multi/eng/C01_293675/2f636a656e6d2f434c49502f45412f423132303139353833342f423132303139353833345f455049303030315f30315f7433352e6d7034/0-0-0/content.mp4?solexpire=1584451800&solpathlen=148&soltoken=5ae15951101d0edcbee3603e5a25426e&soltokenrule=c29sZXhwaXJlfHNvbHBhdGhsZW58c29sdXVpZA==&soluriver=2&soluuid=41f663db-0305-4e0e-b336-7d30a3387b39&itemtypeid=35&tid=rmcPlayer_15844086010118743'
# urllib.request.urlretrieve(url, 'c:/informs/video/test.mp4')

driver.implicitly_wait(10) # seconds
driver.get('https://tv.naver.com/v/11789515/list/552637')
se = driver.find_element_by_xpath('//*[@id="player"]/div/div/div[11]/div[13]/video')

print(se)
