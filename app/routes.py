from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, login_required, current_user, logout_user

from app import app, bcrypt, db
from app.forms import RegisterForm, LoginForm, PasswordResetRequestForm, ResetPasswordForm
from app.email import send_reset_password_mail
from app.models import User

@app.route('/')
@login_required
def index():
    return render_template('index.html')
    ## 不必要的功能测试
    ## title = 'Flask Web App'
    ## paragraphs = ['Section1', 'Section2', 'Section3']
    # 使用title变量，将其中的变量传递到html中
    # data会向前端传递其中的变量
    # return render_template('index.html', title=title, data=paragraphs)


@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()
    # 判断是否有提交
    if form.validate_on_submit():
        # 从wtf表格中获取数据
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Congrats, registeration success', category='success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        #检查密码是否相同
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            # 用户存在且密码相同
            login_user(user, remember=remember)
            flash('Login successed', category='info')
            if request.args.get('next'):
                next_page = request.args.get('next')
                return redirect(next_page)
            return redirect(url_for('index'))
        flash('User not exists or password not match', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/send_password_reset_request', methods=['GET','POST'])
def send_password_reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        token = user.generate_reset_password_token()
        send_reset_password_mail(user, token)
        flash('Password reset request mail is sent, please chech your mailbox', category='info')
    return render_template('send_password_reset_request.html', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user = User.check_reset_password_token(token)
        if user:
            user.password = bcrypt.generate_password_hash(form.password.data)
            db.session.commit()
            flash('Your password has been reset', category='info')
            return redirect(url_for('login'))
        else:
            flash('The user is not exist', category='info')
            return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

