from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import data_required, ValidationError, EqualTo, Email
from app.models import User

class LoginForm(FlaskForm):    
    username = StringField('Usuário', validators=[data_required()])
    password = PasswordField('Senha', validators=[data_required()])
    remember_me = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')

class RegistrationForm(FlaskForm):
    username = StringField('Usuário', validators=[data_required()])
    password = PasswordField('Senha', validators=[data_required()])
    remember_me = BooleanField('Repita a senha', validators=[data_required(), EqualTo('password')])
    submit = SubmitField('Registrar')

    def validar_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not True:
            raise ValidationError('Por favor, use um nome de usuário diferente.')
        
class BookForm(FlaskForm):
    title = StringField('Título', validators=[data_required()])
    author = StringField('Autor', validators=[data_required()])
    genero = StringField('Gênero', validators=[data_required()])
    available = BooleanField('Disponível')
    submit = SubmitField('Salvar')

class PersonForm(FlaskForm):
    nome = StringField('Nome', validators=[data_required()])
    sobrenome = StringField('Sobrenome', validators=[data_required()])
    email = StringField('Email', validators=[data_required(), Email()])
    submit = SubmitField('Salvar')

class BorrowForm(FlaskForm):
    book_id = SelectField('Livro', coerce=int, validators=[data_required()])
    person_id = SelectField('Pessoa', coerce=int, validators=[data_required()])
    submit = SubmitField('Salvar')