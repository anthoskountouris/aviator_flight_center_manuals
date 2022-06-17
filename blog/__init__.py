from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'db5821567f7f382d2883960140f805c2da33e9bffd7b78d6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes

from flask_admin import Admin
from blog.views import AdminView
from blog.models import User
admin = Admin(app,name='Admin panel',template_mode='bootstrap3')
admin.add_view(AdminView(User, db.session))
