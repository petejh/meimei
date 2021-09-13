import imghdr
import os

import deepen
import numpy as np
from PIL import Image

from flask import (
    abort,
    Blueprint,
    current_app,
    redirect,
    render_template,
    request,
    url_for,
)

home_bp = Blueprint('home_bp', __name__, template_folder='templates')

def detect_image(stream):
    header = stream.read(32)
    stream.seek(0)
    format = imghdr.what(None, header)

    # imghdr can fail to detect certain JPEGs (https://bugs.python.org/issue16512).
    # Magic number for JPEG images (https://en.wikipedia.org/wiki/List_of_file_signatures).
    if not format and header.startswith(b'\xff\xd8'):
        format = 'jpg'

    current_app.logger.info(f'Detected image {format=}')
    return format

def get_model():
    here = os.path.dirname(os.path.abspath(__file__))
    model_file = "../models/model.h5"
    model_path = os.path.normpath(os.path.join(here, model_file))

    current_app.logger.info(f'Loading model from file: {model_path}')
    model = deepen.Model()
    model.load(model_path)
    current_app.logger.info(f'{model.layer_dims=}')
    return model

@home_bp.route('/', methods=['GET'])
def home():
    return render_template('index.html.jinja2', title='Home', prediction='???')

@home_bp.route('/', methods=['POST'])
def predict():
    upload = request.files['file']
    if not upload:
        return redirect(url_for('home_bp.home'))
    if detect_image(upload.stream) not in current_app.config['IMAGE_FORMATS']:
        current_app.logger.error(f'Uploaded file is not a valid image.')
        abort(400, 'Not a valid image.')

    model = get_model()

    image= Image.open(upload.stream).resize((64, 64))
    current_app.logger.info(f'{image.size=}, {image.mode=}')
    image_data = np.asarray(image).reshape((64*64*3, 1)) / 255
    current_app.logger.info(f'{image_data.shape=}')

    prob = model.predict(image_data)
    prediction = 'a cat' if prob.all() else 'not a cat'

    return render_template('index.html.jinja2', title='Home', prediction=prediction)
