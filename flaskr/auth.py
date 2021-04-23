from flask import Blueprint
from flask import render_template, request, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from flask import flash
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)
