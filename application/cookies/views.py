from . import cookies
from flask import render_template

@cookies.route('/cookies')
def index():
  cookies = [
    {
      "name": "Chocolate Chip",
      "price": "5.99"
    },
    {
      "name": "Yo Mama",
      "price": "11.59"
    }
  ]
  return render_template('cookies/index.html', cookies=cookies)