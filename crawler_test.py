import crawler

if __name__ == "__main__" :
    Clips = [] # 클립

    url1 = 'https://tv.naver.com/v/12286767/list/565077' # 방법 1화
    # url2 = 'https://tv.naver.com/v/11735321/list/551109' # 관찰카메라24 119화
    crawler.crawler(Clips, url1)

