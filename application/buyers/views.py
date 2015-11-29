# from flask import send_static_file
from . import buyers
from flask import render_template

@buyers.route('/buyers')
def index():
  return render_template('buyers/index.html', buyers=[])