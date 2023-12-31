"""Using flask to build a backend for the Acalypha website for HIP group project"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app ():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "BVCJEFHHKBWEIBVKEDBVUBVKJWDVUBEWJVHEN KERBGFBGKBWDIHVKRWDNVIERHFBNERKHV"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    with app.app_context():
        db.create_all()
    return app


