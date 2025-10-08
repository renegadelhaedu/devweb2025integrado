from flask import *

app = Flask(__name__)
app.secret_key = 'KJH#45K45JHQASs'
crushs = []

usuarios = []
pessoa = 'Evilly'

@app.route('/')
def home_page():
    return render_template('say.html')

@app.route('/cadastrocrush')
def cadastro_crush():
        return render_template('cadastrocrush.html')


@app.route('/verificarsenha', methods=['post','get'])
def verificar_senha():

    if request.method == 'GET':
        return render_template('saysenha.html')
    else:
        login = request.form.get('login')
        senha = request.form.get('senha')
        if login == 'admin' and senha == '123':
            session['login'] = login
            return render_template('logado.html')
        else:
            return render_template('say.html')

@app.route('/adicionar', methods=['post'])
def adicionar_crush():
    #torna a variável modificável no escopo global
    global crushs
    nome = request.form.get('nome')
    idade = request.form.get('idade')
    insta = request.form.get('insta')
    cidade = request.form.get('cidade')

    crushs.append([nome, idade, insta, cidade])
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

    if 'login' in session and session['login'] == 'admin':
        if len(crushs) > 0:
            return render_template('listarcrushs.html', lista=crushs, pessoa=pessoa)
        else:
            return render_template('listarcrushs.html',  pessoa=pessoa)
    else:
        return render_template('say.html')

@app.route('/acharamor', methods=['post'])
def verificar_amado():
    nome_pessoa = request.form.get('candidato')
    if nome_pessoa.lower() in crushs:
        return render_template('saysim.html')
    else:
        return render_template('saynao.html')


@app.route('/detalhes')
def mostrar_detalhes():
    insta = request.values.get('insta')
    achei = None
    for user in crushs:
        if insta == user[2]:
            achei = user
            break

    return render_template('detalhescrush.html', usuario=achei)


if __name__ == '__main__':
    app.run()