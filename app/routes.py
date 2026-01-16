from flask import render_template, redirect, url_for, flash, jsonify
from flask_login import login_user, current_user, login_required
from app import db
from app.models import *
from app.forms import *
from flask import current_app as app
from datetime import datetime


@app.route('/')
@login_required
def index():
    return "Hello world"

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template(
        "login.html",
        form = form
        )