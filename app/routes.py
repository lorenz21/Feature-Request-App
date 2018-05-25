from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm, RequestForm, EditRequestForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Feature
from werkzeug.urls import url_parse
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
# @login_required
def index():
    return render_template('index.html')
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index', user_id=current_user.id)
        return redirect(next_page)
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Welcome, you are now a registered user.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    user = current_user
    return render_template('user.html', user=user)

@app.route('/display/requests/<user_id>')
@login_required
def display_requests(user_id):
    user = current_user
    features = Feature.query.filter_by(user_id=user.id).all()
    return render_template('requests.html', features=features, user=user)

@app.route('/delete/requests/<feature_id>', methods=['GET', 'POST'])
@login_required
def delete_request(feature_id):
    feature_request = Feature.query.get(feature_id)
    if request.method == 'POST':
        db.session.delete(feature_request)
        db.session.commit()
        flash('Feature Request deleted successfully')
        return redirect(url_for('display_requests', user_id=current_user.id))
    return render_template('delete_request.html', feature_request=feature_request, feature_id=feature_id)

@app.route('/edit/requests/<feature_id>', methods=['GET', 'POST'])
@login_required
def edit_request(feature_id):
    feature_request = Feature.query.get(feature_id)
    form = EditRequestForm(obj=feature_request)
    if form.validate_on_submit():
        feature_request.title = form.title.data
        feature_request.description = form.description.data
        feature_request.product_area = form.product_area.data
        feature_request.clients = form.clients.data
        feature_request.target_date = form.target_date.data
        feature_request.priority = form.priority.data
        db.session.add(feature_request)
        db.session.commit()
        flash('Your feature request has been updated.')
        return redirect(url_for('display_requests', user_id=current_user.id))
    return render_template('edit_request.html', feature_request=feature_request, feature_id=feature_id, form=form)

@app.route('/add/requests/<username>', methods=['GET', 'POST'])
@login_required
def add_request(username):
    form = RequestForm()
    if form.validate_on_submit():
        feature = Feature(title=form.title.data, 
        description=form.description.data,
        product_area=form.product_area.data,
        clients=form.clients.data,
        priority=form.priority.data,
        target_date=form.target_date.data, 
        requestor=current_user)
        db.session.add(feature)
        db.session.commit()
        flash('Your feature request has been recorded.')
        return redirect(url_for('display_requests', user_id=current_user.id))
    return render_template('add_request.html', user=user, form=form)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()