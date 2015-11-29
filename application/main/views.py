# from flask import send_static_file
from . import main
from flask import render_template

@main.route('/')
def index():
  return render_template('index.html')

@main.route('/static/<path:path>')
def asset(path):
  return current_app.send_static_file(path)