import os
# 从.env中获取所有信息
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    #SECRET KEY
    SECRET_KEY = os.getenv('SECRET_KEY')
    #reCAPCHA PUBLIC KEY
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    #reCAPCHA PRIVATE KEY
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
    # 数据库设置
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # Flask Gmail 设置
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_DEBUG = True
    MAIL_USERNAME = os.getenv('GMAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')