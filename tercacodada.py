from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('tercacodada.html')


@app.route('/logar', methods=['post'])
def logar_usuario():
    login = request.form.get('loginusuario')
    senha = request.form.get('senhausuario')

    if login == 'sayonara' and senha == 'minhaamiganayara':
        return render_template('homepage.html')
    else:
        mensagem = 'Usuário e senha incorretos'
        return render_template('tercacodada.html', msg=mensagem)

app.run()