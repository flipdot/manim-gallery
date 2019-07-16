import importlib
import inspect

import manimlib
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
    image = render_scene(module)
    code = inspect.getsource(module)
    example = {
        'title': id_,
        'image': image,
        'code': highlight(code, Python3Lexer(), HtmlFormatter())
    }
    return render_template('detail.html', example=example, style=HtmlFormatter().get_style_defs('.highlight'))


def render_scene(module):
    print(inspect.getmembers(module))
    scene_classes = manimlib.extract_scene.get_scene_classes_from_module(module)
    # This is here because it was removed inside of manim:
    # https://github.com/3b1b/manim/commit/4fa782b8b5f16378a8352315b7975581b9fd87fe#r33417433
    scene_classes = [x for x in scene_classes if x.__module__.startswith(module.__name__)]
    print(scene_classes)
    # config = {
    #     'movie_file_extension': '.gif',
    #     'file_name': module,
    #     'input_file_path': args.file,
    # }
    # config = {
    #     'camera_config': {
    #         "pixel_height": 1440,
    #         "pixel_width": 2560,
    #     },
    #     'file_writer_config': {
    #         'input_file_path': 'wololo.mp4'
    #     },
    #     'skip_animations': None,
    #     'start_at_animation_number': None,
    #     'end_at_animation_number': None,
    #     'leave_progress_bars': None,
    # }
    config = {'camera_config': {'frame_rate': 60, 'pixel_height': 1440, 'pixel_width': 2560},
              'end_at_animation_number': None,
              'file_writer_config': {'file_name': None,
                                     'input_file_path': 'src/examples/hello_world.py',
                                     'movie_file_extension': '.mp4',
                                     'png_mode': 'RGB',
                                     'save_as_gif': False,
                                     'save_last_frame': False,
                                     'save_pngs': False,
                                     'write_to_movie': True},
              'leave_progress_bars': False,
              'skip_animations': False,
              'start_at_animation_number': None}
    for SceneClass in scene_classes:
        scene = SceneClass(**config)
    manimlib.extract_scene.main(config)
    return 'http://placekitten.com/600/600'
