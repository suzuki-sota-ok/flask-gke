from flask import Flask
from .views.home import home_bp, todo_bp

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(home_bp)
    app.register_blueprint(todo_bp)
    
    return app