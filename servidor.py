#importei o pacote para criar app web
from flask import *

#instanciei o objeto Flask
app = Flask(__name__)

#criando uma rota endpoint
@app.route('/')
def pagina_principal():
    return render_template('segundodia.html')

@app.route('/maisinfo')
def saber_suino():
    return render_template('terceirodia.html')

#executando o servidor
app.run(host='0.0.0.0')



