import importlib
import inspect
import pkgutil
from pathlib import Path

import manimlib
from flask import Flask, render_template, abort, url_for, send_from_directory
from flask_assets import Environment, Bundle
from pygments import highlight
from pygments.lexers.python import Python3Lexer
from pygments.formatters.html import HtmlFormatter
from flask_frozen import Freezer

import examples

CAMERA_CONFIG = {
    'xs': {'frame_rate': 12, 'pixel_height': 240, 'pixel_width': 320},
    'm': {'frame_rate': 24, 'pixel_height': 480, 'pixel_width': 640},
    'l': {'frame_rate': 30, 'pixel_height': 720, 'pixel_width': 1280},
    'xl': {'frame_rate': 30, 'pixel_height': 1080, 'pixel_width': 1920},
}

app = Flask(__name__)
app.config['RENDERINGS_PATH'] = Path('media/renderings')
app.config['EXAMPLES_PATH'] = Path('examples/')

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('main.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)


@app.route('/')
def index():
    path = Path(examples.__path__[0])
    category_names = [x.name for x in pkgutil.iter_modules([path]) if x.ispkg]

    def get_examples(category):
        return [x.split('.')[-1] for x in examples.__all__ if x.startswith(category)]

    categories = [
        {
            'name': category,
            'examples': [
                {
                    'title': module_name,
                    'image': get_scene_details(category, importlib.import_module(f'examples.{category}.{module_name}'))[0],
                    'module_name': module_name,
                } for module_name in get_examples(category)
            ]
        } for category in category_names
    ]
    return render_template('index.html', categories=categories)


@app.route('/detail/<category>/<module_name>/')
def detail(category, module_name):
    if f'{category}.{module_name}' not in examples.__all__ or module_name.startswith('_'):
        abort(404)
    module = importlib.import_module(f'examples.{category}.{module_name}')
    code = inspect.getsource(module)
    example = {
        'title': module_name,
        'scenes': get_scene_details(category, module),
        'code': highlight(code, Python3Lexer(), HtmlFormatter()),
        'filename': f'{module_name}.py',
        'category': category,
    }
    return render_template('detail.html', example=example, style=HtmlFormatter().get_style_defs('.highlight'))


@app.route('/renderings/<size>/<category>/<module_name>/<scene_name>.gif')
def renderings(size, category, module_name, scene_name):
    try:
        module = importlib.import_module(f'examples.{category}.{module_name}')
    except ModuleNotFoundError:
        return abort(404)
    scene_classes = [x for x in get_scene_classes(module) if x.__name__ == scene_name]
    if len(scene_classes) != 1:
        return abort(404)
    SceneClass = scene_classes[0]

    if size not in CAMERA_CONFIG:
        return abort(404)

    config = {'camera_config': CAMERA_CONFIG[size],
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


@app.route('/example_src/<category>/<filename>')
def example_src(category, filename):
    return send_from_directory(app.config['EXAMPLES_PATH'] / category, filename)


def get_scene_details(category, module):
    scene_classes = get_scene_classes(module)

    def get_url(scene, size):
        return url_for('renderings', category=category, module_name=module.__name__.rsplit('.')[-1], scene_name=scene.__name__, size=size)

    return [
        {
            'image_url': {size: get_url(scene, size) for size in CAMERA_CONFIG.keys()},
            'name': scene.__name__,
        } for scene in scene_classes]


def get_scene_classes(module):
    scene_classes = manimlib.extract_scene.get_scene_classes_from_module(module)
    # This is here because it was removed inside of manim:
    # https://github.com/3b1b/manim/commit/4fa782b8b5f16378a8352315b7975581b9fd87fe#r33417433
    return [x for x in scene_classes if x.__module__.startswith(module.__name__)]


if __name__ == '__main__':
    freezer = Freezer(app)

    if __name__ == '__main__':
        freezer.freeze()
