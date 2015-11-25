# from flask import send_static_file
from . import main
from flask import current_app

@main.route('/')
def index():
  return current_app.send_static_file('index.html')

@main.route('/static/<path:path>')
def asset(path):
  return current_app.send_static_file(path)