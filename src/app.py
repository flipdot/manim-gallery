from flask import Flask, render_template
from flask_assets import Environment, Bundle
from pygments import highlight
from pygments.lexers.python import Python3Lexer
from pygments.formatters.html import HtmlFormatter

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
    code = """
from manimlib.shortcuts import *

class AwesomeAnimation(Scene):
    pass
    """
    example = {
        'title': id_,
        'image': 'http://placekitten.com/600/600',
        'code': highlight(code, Python3Lexer(), HtmlFormatter())
    }
    return render_template('detail.html', example=example, style=HtmlFormatter().get_style_defs('.highlight'))
