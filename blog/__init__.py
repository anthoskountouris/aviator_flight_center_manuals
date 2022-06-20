from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'db5821567f7f382d2883960140f805c2da33e9bffd7b78d6'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://prjodyzuemtpkf:268b9165667f6a4223428dce075923e957d7b647b998f01ec834d9b835e263a7@ec2-3-224-8-189.compute-1.amazonaws.com:5432/dcieekucnlbcat'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes

from flask_admin import Admin
from blog.views import AdminView
from blog.models import User
admin = Admin(app,name='Admin panel',template_mode='bootstrap3')
admin.add_view(AdminView(User, db.session))
