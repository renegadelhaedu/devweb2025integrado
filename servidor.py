#importei o pacote para criar app web
from flask import *

#instanciei o objeto Flask
app = Flask(__name__)

#criando uma rota endpoint
@app.route('/')
def pagina_principal():
    return render_template('minhasfesta.html')

@app.route('/maisinfo')
def saber_suino():
    return render_template('terceirodia.html')

@app.route('/verificar')
def verificar_convidado():
    #pega o valor do campo que veio da requisição do cliente
    nome = request.values.get('nomepessoa')

    convidados = ['tevez','cassio','ronaldo','romero']

    #coloca o nome do usuário em minúsculo e compara
    if nome.lower() in convidados:
        return render_template('foiconvidado.html')
    else:
        return render_template('naofoiconvidado.html')


#executando o servidor
app.run()



