from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Nome Completo :', [validators.Length(min=4, max=25)])
    username = StringField('Usuario', [validators.Length(min=4, max=25)])
    email = StringField('Email :', [validators.Length(min=6, max=35)])
    password = PasswordField('Nova Senha', [
        validators.DataRequired(),
        validators.EqualTo('confirmação da senha', message='senhas não iguais')
    ])
    confirm = PasswordField('Repetir senha')