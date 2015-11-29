# from flask import send_static_file
from . import cookies
from flask import render_template

@cookies.route('/cookies')
def index():
  return render_template('cookies/index.html', cookies=[])