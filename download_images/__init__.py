from flask import Flask


def create_app(test_config = None):
    app = Flask(__name__)
    app.secret_key = "Test123"

    from . import download_images
    app.register_blueprint(download_images.di)

    return app
