from flask import Flask
from flask_wtf import FlaskForm 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from shop import routes
app = Flask(__name__)


app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
