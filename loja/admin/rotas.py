from turtle import title
from flask import render_template, session, request, redirect, url_for,flash


from loja import app, db, bcrypt
from .forms import RegistrationForm
import os
from .models import User



@app.route('/')
def home():
    return "Pagina Inicial Flask"



@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data,username=form.username.data,email=form.email.data,
        password=hash_password)
        db.session.add(user)
        flash('Cadastro completo')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title="Pagina de Cadastro")