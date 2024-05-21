from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../instance/config.py')

    from .auth import auth_bp
    from .routes import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app
