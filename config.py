from os import getenv, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

LOG_LEVEL = getenv('LOG_LEVEL', 'INFO')

MAX_CONTENT_LENGTH = 1024 * 1024
IMAGE_FORMATS = ['jpeg', 'jpg', 'png']
