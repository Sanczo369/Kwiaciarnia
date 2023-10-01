from flask import Flask
from flask_wtf import FlaskForm 
from wtforms import StringField, EmailField, TelField, PasswordField, TextAreaField, BooleanField
app = Flask(__name__)


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
@app.route('/') 
def index(): 
    return '<h1>Hello World!!!</h1>' 

if __name__ == '__main__': 
    app.run()