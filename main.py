import random

from flask import Flask, render_template, request

import database as db

app = Flask(__name__, template_folder='templates')
app.secret_key = 'MSG'
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


@app.route('/')
def index():
    views = db.get_thumbnail_high_views()
    hashtag = []
    for i in views:
        temp = db.get_hashtag(i[0])
        if len(temp) > 3:
            temp = random.sample(temp, 3)
        hashtag.append(temp)
    html = render_template('index.html', data_list=views, tag_list=hashtag)
    return html


@app.route('/vod', methods=['POST'])
def vod():
    vod_id = request.form['test']
    print(vod_id)
    vod = db.get_vod(vod_id)
    print(vod)
    thum_list = db.get_thumbnail_with_vodid(vod_id)
    if len(thum_list) > 3:
        thum_list = random.sample(thum_list, 3)

    print(thum_list)
    print(thum_list[0][4].seconds)
    hashtag = []
    for i in thum_list:
        temp = db.get_hashtag(i[0])
        if len(temp) > 3:
            temp = random.sample(temp, 3)
        hashtag.append(temp)
    print(hashtag)
    html = render_template('vod.html', vod_id=vod, data_list=thum_list, tag_list=hashtag)
    return html


@app.route('/info', methods=['GET', 'POST'])
def info():
    search = request.args.get('search')
    search_vod = db.get_vod_cover(search)
    views = db.get_thumbnail_from_hashtag(search)
    hashtag = []
    for i in views:
        temp = db.get_hashtag(i[0])
        if len(temp) > 2:
            temp = random.sample(temp, 2)
        hashtag.append(temp)
    print(search_vod)
    html = render_template('info.html', search_arg=search_vod, search_origin=search, data_list=views, tag_list=hashtag)
    return html


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    html = render_template('admin.html')
    return html


@app.route('/test', methods=['GET', 'POST'])
def test():
    html = render_template('test.html')
    return html


@app.route('/admin/crawler', methods=['GET', 'POST'])
def crawler():
    search = request.args.get('vod_search')
    search_vod = db.get_vod_cover(search)
    print(search_vod)
    html = render_template('crawler.html', data_list=search_vod)
    return html


@app.route('/admin/scheduler', methods=['GET', 'POST'])
def scheduler():
    thum_list = db.get_thumbnail_with_vodid(4)
    print(thum_list)
    html = render_template('scheduler.html', thum_list=thum_list)
    return html


@app.route('/admin/register', methods=['GET', 'POST'])
def register():
    thum_list = db.get_thumbnail_with_vodid(4)
    print(thum_list)
    hashtag = []
    for i in thum_list:
        temp = db.get_hashtag(i[0])
        if len(temp) > 7:
            temp = random.sample(temp, 7)
        hashtag.append(temp)
    print(hashtag)
    html = render_template('register.html', thum_list=thum_list, hash_list=hashtag)
    return html


@app.route('/hidden', methods=['GET', 'POST'])
def hidden():
    html = render_template('hidden.html')
    return html


app.run(host='127.0.0.1', port=8080)
