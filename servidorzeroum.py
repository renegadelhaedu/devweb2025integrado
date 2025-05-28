from flask import *

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('dataniver.html')


@app.route('/saberano', methods=['post'])
def saber_ano():
    idade_user = request.form.get('idade')
    ano = 2025 - int(idade_user)
    return render_template('anoniver.html', ano_user=ano)

app.run()