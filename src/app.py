from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('main.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)


@app.route('/')
def index():
    examples = [
        {
            'title': i,
            'image': 'http://placekitten.com/150/150',
            'id': i
        } for i in range(50)
    ]
    return render_template('index.html', examples=examples)


@app.route('/detail/<id_>')
def detail(id_):
    example = {
        'title': id_,
        'image': 'http://placekitten.com/600/600'
    }
    return render_template('detail.html', example=example)
