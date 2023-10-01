from flask import Flask
from flask_wtf import FlaskForm 
from wtforms import StringField, EmailField, TelField, PasswordField, TextAreaField, BooleanField
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


class RegistrationForm(FlaskForm):
    name = StringField('Imię', render_kw={"placeholder": "Imię"})
    surname = StringField('Nazwisko', render_kw={"placeholder": "Nazwisko"})
    email = EmailField('E-mail', render_kw={"placeholder": "E-mail"})
    phone = TelField('Telefon', render_kw={"placeholder": "Telefon"})
    password = PasswordField('Tekst', render_kw={"placeholder": "text"})

class LoginForm(FlaskForm):
    email = EmailField('E-mail', render_kw={"placeholder": "E-mail"})
    password = PasswordField('Tekst', render_kw={"placeholder": "******"})
    remember = BooleanField('Zapamiętaj mnie')
    
class NewsletterForm(FlaskForm):
    email = EmailField('E-mail', render_kw={"placeholder": "E-mail"}) 
    
class ContactForm(FlaskForm):
    name = StringField('Imię', render_kw={"placeholder": "Imię"})
    email = EmailField('E-mail', render_kw={"placeholder": "E-mail"})
    phone = TelField('Telefon', render_kw={"placeholder": "Telefon"})
    password = TextAreaField('Tekst', render_kw={"placeholder": "..."})  
    
    
    
# Tabele
class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100)) 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100)) 
    surname = db.Column(db.String(100))
    email = db.Column(db.String(100))  
    phone = db.Column(db.String(100))
    password = db.Column(db.String(100))
    
@app.route('/') 
def index(): 
    return '<h1>Hello World!!!</h1>' 

if __name__ == '__main__': 
    app.run()