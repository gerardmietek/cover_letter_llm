from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ug791dvuhh-19efha-fafwaf3f0h1df'

    return app