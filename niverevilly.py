from flask import *

app = Flask(__name__)
crushs = ['mateus kaio','diego','pedro','luis antonio','miguel']
usuarios = []
pessoa = 'Evilly'

@app.route('/')
def home_page():
    return render_template('say.html')

@app.route('/administradora')
def mostrar_pag_senha():
    return render_template('saysenha.html')

@app.route('/verificarsenha', methods=['post'])
def verificar_senha():
    senha = request.form.get('senha')
    if senha == 'sa':
        return render_template('logado.html')
    else:
        return render_template('say.html')

@app.route('/adicionar', methods=['post'])
def adicionar_crush():
    #torna a variável modificável no escopo global
    global crushs
    nome = request.form.get('nome')
    #adicionar dentro da lista
    crushs.append(nome)
    mensagem = nome + ' foi adicionado com sucesso'
    return render_template('logado.html', msg=mensagem)


@app.route('/adicionarusuario', methods=['post'])
def adicionar_usuario():
    #torna a variável modificável no escopo global
    global usuarios
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    email = request.form.get('email')

    usuarios.append([nome, senha, email])
    mensagem = nome + ' foi adicionado com sucesso'
    return render_template('logado.html', msg=mensagem)



@app.route('/remover', methods=['post'])
def remover_crush():
    #torna a variável modificável no escopo global
    global crushs
    nome = request.form.get('nome')
    if nome in crushs:
        crushs.remove(nome)

    else:
        msg = 'nao consta na lista de crushs'

    return render_template('logado.html')

@app.route('/listarcrushs', methods=['get'])
def listar_cruchs():
    if len(crushs) > 0:
        return render_template('listarcrushs.html', lista=crushs, pessoa=pessoa)


@app.route('/acharamor', methods=['post'])
def verificar_amado():
    nome_pessoa = request.form.get('candidato')
    if nome_pessoa.lower() in crushs:
        return render_template('saysim.html')
    else:
        return render_template('saynao.html')

if __name__ == '__main__':
    app.run()