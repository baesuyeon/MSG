from flask import Flask, render_template, request
import database as db
import random

app = Flask(__name__, template_folder='templates')
app.secret_key = 'MSG'
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


@app.route('/')
def index():
    views = db.get_thumbnail_high_views()
    hashtag = []
    for i in views:
        temp = db.get_hashtag(i[0])
        if len(temp) > 2:
            temp = random.sample(temp, 2)
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
    if len(thum_list) > 2:
        thum_list = random.sample(thum_list, 2)

    print(thum_list)
    hashtag = []
    for i in thum_list:
        temp = db.get_hashtag(i[0])
        if len(temp) > 2:
            temp = random.sample(temp, 2)
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


app.run(host='127.0.0.1', port=8080)
