from . import distributors
from flask import render_template

@distributors.route('/distributors')
def index():
  dists = [
    {
      "name": "Guy 1",
      "address": "Place 1"
    },
    {
      "name": "Guy 2",
      "address": "Place 2"
    }
  ]
  return render_template('distributors/index.html', distributors=dists)