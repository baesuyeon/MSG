class Clip :
    def __init__(self):
        self.clip_title = "" # 클립 제목
        self.clip_views = 0 # 클립 조회수
        self.clip_time = 0 # 클립 길이
        self.clip = "" # 클린 영상 경로

    def add_title(self, title):
        self.clip_title = title

    def add_views(self, view):
        self.clip_views = view

    def add_time(self, time):
        self.clip_time = time

    def add_clip(self, clip_url):
        self.clip = clip_url

    def get_title(self):
        return self.clip_title

    def get_views(self):
        return self.clip_views

    def get_time(self):
        return self.clip_time

    def get_clip(self):
        return self.clip

""""
class ClipHash : # 클립 & 해시
    def __init__(self):
        clip_hash = {}

    def add(self, clip_id, hash_id):
        self.clip_hash[clip_id] = hash_id
"""

class Hash :
    hashs = [] # 클립 해시

    def add_hash(self, item):
        self.hashs.append(item)

    def get_hash(self):
        return self.hashs