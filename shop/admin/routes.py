from flask import render_template, session, request, redirect, url_for, flash

from shop import app, db
from .forms import RegistrationForm
@app.route('/') 
def home(): 
    return render_template('index.html')

@app.route('/register', methods=['GET', "POST"])
def register():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title="Strona Rejestracji")