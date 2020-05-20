# 从Flask库中导入flask
# 使用render_template，从templates文件夹中载入html渲染界面
# 由于flask_bootstrap的限制，bootstrap只能使用3.3
# SQLAlchemy的更新，使得在建立数据库时，无须使用导入DataTime，直接调用命令即可
# 使用datetime库，在向数据库写入信息时，记录数据时间
from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
from flask_mail import Mail, Message
from datetime import datetime

import os

from config import Config




# 启动相对应的app
app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'You must login to access this page'
login.login_message_category = 'info'


from app.routes import *

