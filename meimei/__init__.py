__version__ = '0.1.0'

from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile('../config.py')

    with app.app_context():
        app.logger.setLevel(app.config['LOG_LEVEL'])

        from .home import home_bp
        app.register_blueprint(home_bp)

        return app
