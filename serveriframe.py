from flask import *


app = Flask(__name__)


@app.route('/')
def pagina_principal():
    return render_template('introiframe.html')

@app.route('/paginacadastro')
def mostrar_pag_cadastro():
    return render_template('paginacadastro.html')

@app.route('/login')
def mostrar_pag_login():
    return render_template('paginacadastro.html')

if '__main__' == __name__:
    app.run()