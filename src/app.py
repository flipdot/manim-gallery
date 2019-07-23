import importlib
import inspect
from pathlib import Path

import manimlib
from flask import Flask, render_template, abort, url_for, send_from_directory
from flask_assets import Environment, Bundle
from pygments import highlight
from pygments.lexers.python import Python3Lexer
from pygments.formatters.html import HtmlFormatter
from flask_frozen import Freezer

import examples

app = Flask(__name__)
app.config['RENDERINGS_PATH'] = Path('media/renderings')

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('main.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)


@app.route('/')
def index():
    example_list = [
        {
            'title': module,
            'image': get_rendering_urls(importlib.import_module(f'examples.{module}'), size='xs')[0],
            'id': module
        } for module in examples.__all__ if not module.startswith('_')
    ]
    return render_template('index.html', examples=example_list)


@app.route('/detail/<id_>/')
def detail(id_):
    if id_ not in examples.__all__ or id_.startswith('_'):
        abort(404)
    module = importlib.import_module(f'examples.{id_}')
    code = inspect.getsource(module)
    example = {
        'title': id_,
        'images': get_rendering_urls(module),
        'code': highlight(code, Python3Lexer(), HtmlFormatter()),
        'filename': f'{id_}.py',
    }
    return render_template('detail.html', example=example, style=HtmlFormatter().get_style_defs('.highlight'))


@app.route('/renderings/<size>/<module_id>/<scene_name>.gif')
def renderings(size, module_id, scene_name):
    try:
        module = importlib.import_module(f'examples.{module_id}')
    except ModuleNotFoundError:
        return abort(404)
    scene_classes = [x for x in get_scene_classes(module) if x.__name__ == scene_name]
    if len(scene_classes) != 1:
        return abort(404)
    SceneClass = scene_classes[0]

    camera_config = {
        'xs': {'frame_rate': 12, 'pixel_height': 240, 'pixel_width': 320},
        'm': {'frame_rate': 24, 'pixel_height': 480, 'pixel_width': 640},
    }

    if size not in camera_config:
        return abort(404)

    config = {'camera_config': camera_config[size],
              'end_at_animation_number': None,
              'file_writer_config': {'file_name': None,
                                     'input_file_path': module.__file__,
                                     'movie_file_extension': '.mp4',
                                     'png_mode': 'RGB',
                                     'save_as_gif': True,
                                     'save_last_frame': False,
                                     'save_pngs': False,
                                     'write_to_movie': True},
              'leave_progress_bars': False,
              'skip_animations': False,
              'start_at_animation_number': None,
              'video_output_dir': None,
              'video_dir': app.config['RENDERINGS_PATH'],
              'tex_dir': 'video_tex',
              'media_dir': 'video_media',
              'module': None,
              }
    manimlib.constants.initialize_directories(config)

    # Instantiating the class actually renders the scene
    scene = SceneClass(**config)

    path = Path(scene.file_writer.gif_file_path)
    directory = path.parent
    filename = path.name
    return send_from_directory(directory, filename)


def get_rendering_urls(module, size='m'):
    scene_classes = get_scene_classes(module)
    return [
        {
            'url': url_for('renderings', module_id=module.__name__.rsplit('.')[-1], scene_name=x.__name__, size=size),
            'scene_name': x.__name__,
        } for x in scene_classes]


def get_scene_classes(module):
    scene_classes = manimlib.extract_scene.get_scene_classes_from_module(module)
    # This is here because it was removed inside of manim:
    # https://github.com/3b1b/manim/commit/4fa782b8b5f16378a8352315b7975581b9fd87fe#r33417433
    return [x for x in scene_classes if x.__module__.startswith(module.__name__)]


if __name__ == '__main__':
    freezer = Freezer(app)

    if __name__ == '__main__':
        freezer.freeze()
