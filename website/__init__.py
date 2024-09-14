from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from werkzeug.security import generate_password_hash
from . import config

db = SQLAlchemy()
DB_NAME = config.DB_NAME

app = Flask(__name__)


def create_app():
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from .views import views
    from .auth import auth
    from .api import api

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')

    from .models import User

    with app.app_context():
        db.create_all()

        if len(User.query.all()) == 0:
            new_user = User(
                login='admin',
                password=generate_password_hash(
                    '12345678',
                    method='scrypt'
                )
            )

            db.session.add(new_user)

            db.session.commit()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
