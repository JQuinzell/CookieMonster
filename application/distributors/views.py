# from flask import send_static_file
from . import distributors
from flask import render_template

@distributors.route('/distributors')
def index():
  return render_template('distributors/index.html', distributors=[])