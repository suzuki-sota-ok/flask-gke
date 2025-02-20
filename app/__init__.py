from flask import Flask
from .views.home import home_bp
from .views.todo import todo_bp

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(home_bp)
    app.register_blueprint(todo_bp)
    
    return app