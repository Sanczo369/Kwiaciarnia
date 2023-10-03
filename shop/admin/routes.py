from flask import render_template, session, request, redirect, url_for

from shop import app, db

@app.route('/') 
def home(): 
    return render_template('index.html')

@app.route('/register') 
def home(): 
    return render_template('admin/register.html', title="Rejestracja użytkowników")