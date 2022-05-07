from flask import Blueprint, render_template, redirect, url_for, flash,current_app
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash

from app.auth.decorators import admin_required
from app.db import db
from app.db.models import User

auth = Blueprint('auth', __name__, template_folder='templates')






