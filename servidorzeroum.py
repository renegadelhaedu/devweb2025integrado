from flask import *

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('dataniver.html')


@app.route('/saberano', methods=['post'])
def saber_ano():
    idade_user = request.form.get('idade')
    ano = 2025 - int(idade_user)



@app.route('/signo', methods=['post'])
def verificar_signo():
    data = request.form.get('datanascimento')
    mes = int(data.split('-')[1])
    dia = int(data.split('-')[2])
    if (dia >= 23 and dia <= 31 and mes == 10) or (dia <=21 and mes==11):
        return 'esse serumaninho é uma criatura escorpianica. Cuidado'

    else:
        return  'pelo menos nao é escorpiao'

app.run()