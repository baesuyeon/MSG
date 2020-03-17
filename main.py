from flask import Flask, render_template, request
import database as db
import random

app = Flask(__name__, template_folder='templates')
app.secret_key = 'MSG'
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

# hi~
# hello

@app.route('/')
def index():
    views = db.get_thumbnail_high_views()
    print(views)
    hashtag = []
    for i in views:
        temp = db.get_hashtag(i[0])
        temp = random.sample(temp, 2)
        hashtag.append(temp)
    print(hashtag)
    html = render_template('index.html', data_list=views, tag_list=hashtag )
    return html

@app.route('/vod', methods=['GET', 'POST'])
def vod():
    html = render_template('vod.html')
    return html


@app.route('/info', methods=['GET', 'POST'])
def info():
    search = request.args.get('search')
    html = render_template('info.html', search_arg=search)
    return html


app.run(host='127.0.0.1', port=8080)
