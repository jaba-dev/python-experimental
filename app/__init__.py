from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Import and register blueprints (routes)
    from .routes import main
    app.register_blueprint(main)

    return app
