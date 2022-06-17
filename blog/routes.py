from flask import render_template, url_for, request, redirect, flash
from blog import app, db
from blog.models import User
from blog.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html')

@app.route("/register",methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data,email=form.email.data,password=form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Registration successful!')
    return redirect(url_for('home'))
  return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      flash('Login successful!')
      return render_template('home.html',form=form)
    flash('Invalid email address or password.')
    
    return render_template('login.html',form=form)

  return render_template('login.html',title='Login',form=form)

@app.route("/aquila_manual")
@login_required
def aquila():
  return render_template('/manuals/aquila_manual.html')

@app.route("/da40_manual")
@login_required
def daforty():
  return render_template('/manuals/da40_manual.html')

@app.route("/logout")
@login_required
def logout():
  logout_user()
  return redirect(url_for('home'))
