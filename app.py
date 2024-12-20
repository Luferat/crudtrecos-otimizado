from flask import Flask
from flask_mysqldb import MySQL
from functions.geral import calcular_idade
from modules.apaga import mod_apaga
from modules.apagausuario import mod_apagausuario
from modules.cadastro import mod_cadastro
from modules.edita import mod_edita
from modules.editaperfil import mod_editaperfil
from modules.index import mod_index
from modules.login import mod_login
from modules.logout import mod_logout
from modules.novasenha import mod_novasenha
from modules.novo import mod_novo
from modules.page_not_found import mod_page_not_found
from modules.perfil import mod_perfil
from modules.start import mod_start

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crudtrecos'

app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_USE_UNICODE'] = True
app.config['MYSQL_CHARSET'] = 'utf8mb4'

mysql = MySQL(app)


@app.before_request
def start():
    mod_start(mysql=mysql)


@app.route("/")
def index():
    return mod_index(mysql=mysql)


@app.route('/novo', methods=['GET', 'POST'])
def novo():
    return mod_novo(mysql=mysql)


@app.route('/edita/<id>', methods=['GET', 'POST'])
def edita(id):
    return mod_edita(mysql=mysql, id=id)


@app.route('/apaga/<id>')
def apaga(id):
    return mod_apaga(mysql, id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return mod_login(mysql=mysql)


@app.route('/logout')
def logout():
    return mod_logout()


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    return mod_cadastro(mysql=mysql)


@app.route('/novasenha', methods=['GET', 'POST'])
def novasenha():
    return mod_novasenha(mysql=mysql)


@app.route('/perfil')
def perfil():
    return mod_perfil(mysql=mysql)


@app.route('/apagausuario')
def apagausuario():
    return mod_apagausuario(mysql=mysql)


@app.route('/editaperfil', methods=['GET', 'POST'])
def editaperfil():
    return mod_editaperfil(mysql=mysql)


@app.errorhandler(404)
def page_not_found(e):
    return mod_page_not_found()


if __name__ == '__main__':
    app.run(debug=True)
