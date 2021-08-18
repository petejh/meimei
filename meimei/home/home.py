import imghdr

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

    prediction = 'a cat'

    return render_template('index.html.jinja2', title='Home', prediction=prediction)
