from application import app
from model import Model
Model.connect('cookiemonster.sqlite')
app.run(debug=True)