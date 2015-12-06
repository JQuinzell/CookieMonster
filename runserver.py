from application import app
from models import Model
Model.connect('cookiemonster.sqlite')
app.run(debug=True)