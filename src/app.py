import importlib
import inspect

from flask import Flask, render_template, abort
from flask_assets import Environment, Bundle
from pygments import highlight
from pygments.lexers.python import Python3Lexer
from pygments.formatters.html import HtmlFormatter

import examples

app = Flask(__name__)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('main.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)


@app.route('/')
def index():
    example_list = [
        {
            'title': module,
            'image': 'http://placekitten.com/150/150',
            'id': module
        } for module in examples.__all__ if not module.startswith('_')
    ]
    return render_template('index.html', examples=example_list)


@app.route('/detail/<id_>')
def detail(id_):
    if id_ not in examples.__all__ or id_.startswith('_'):
        abort(404)
    module = importlib.import_module(f'examples.{id_}')
    code = inspect.getsource(module)
    example = {
        'title': id_,
        'image': 'http://placekitten.com/600/600',
        'code': highlight(code, Python3Lexer(), HtmlFormatter())
    }
    return render_template('detail.html', example=example, style=HtmlFormatter().get_style_defs('.highlight'))
