from turtle import title
from flask import render_template, session, request, redirect, url_for,flash

from loja import app, db
from .forms import RegistrationForm
from loja.admin.forms import RegistrationForm

@app.route('/')
def home():
    return "Seja bem vindo ao home flask"


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = User(form.username.data, form.email.data,
        #           form.password.data)
        #db_session.add(user)
        flash('Cadastro Concluido')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title='Pagina de Registros')