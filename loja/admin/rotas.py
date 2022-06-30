from flask import render_template, session, request, redirect, url_for


from loja import app, db

@app.route('/')
def home():
    return "Pagina Inicial Flask"



@app.route('/registrar')
def registrar():
    return render_template('admin/registrar.html', title="Realização de Cadastros")