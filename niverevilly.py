from flask import *
from utils.auxiliares import *

app = Flask(__name__)
app.secret_key = 'KJH#45K45JHQASs'
crushs = [['pedro', 17, 'phrodrigues','santa cruz','phr','123']]

usuarios = []
pessoa = 'Evilly'

@app.route('/')
def home_page():
    return render_template('say.html')

@app.route('/logincrush', methods=['GET','POST'])
def login_crush():
    if request.method == 'GET':
        return render_template('crush/logincrush.html')

    login = request.form.get('login')
    senha = request.form.get('senha')

    if fazer_login_crush(login, senha, crushs):
        session['crush'] = login
        return render_template('crush/homepagecrush.html', login=login)
    else:
        msg = 'login ou senha incorretos'
        return render_template('crush/logincrush.html', msg=msg)


@app.route('/cadastrocrush', methods=['GET','POST'])
def cadastro_crush():
    if request.method == 'GET':
        return render_template('crush/cadastrocrush.html')

    global crushs

    nome = request.form.get('nome')
    idade = request.form.get('idade')
    insta = request.form.get('insta')
    cidade = request.form.get('cidade')
    login = request.form.get('login')
    senha = request.form.get('senha')

    if not verificar_login_crush(login, crushs):
        crushs.append([nome,idade,insta,cidade,login,senha])
        return render_template('crush/logincrush.html')
    else:
        msg = 'login já existente'
        return render_template('crush/logincrush.html', msg=msg)


@app.route('/logout')
def fazer_logout():
    session.clear()
    return render_template('say.html')

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

    if 'login' not in session:
        return render_template('say.html')
    
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
    print(session['login'])
    for user in crushs:
        if insta == user[2]:
            achei = user
            break

    return render_template('detalhescrush.html', usuario=achei)


if __name__ == '__main__':
    app.run()