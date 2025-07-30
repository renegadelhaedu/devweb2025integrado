from flask import *

app = Flask(__name__)
crushs = ['jose','roberto','caio','italo','miguel']

@app.route('/')
def home_page():
    return render_template('say.html')

@app.route('/administradora')
def mostrar_pag_senha():
    return render_template('saysenha.html')

@app.route('/verificarsenha', methods=['post'])
def verificar_senha():
    senha = request.form.get('senha')
    if senha == 'sayonara2007':
        return render_template('logado.html')
    else:
        return render_template('say.html')



@app.route('/acharamor', methods=['post'])
def verificar_amado():
    nome_pessoa = request.form.get('candidato')
    if nome_pessoa.lower() in crushs:
        return render_template('saysim.html')
    else:
        return render_template('saynao.html')

if __name__ == '__main__':
    app.run()