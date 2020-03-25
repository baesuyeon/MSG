import crawler

if __name__ == "__main__" :
    Clips = [] # 클립
    search_word = '방법 1화' # '방법 1화', '관찰카메라24 119화', '반의반 1화'
    vod_no = 1
    crawler.crawler(Clips, search_word, vod_no)

# //*[@id="player"]/div/div[1]/div[11]/div[13]/video/source
# blob 처리