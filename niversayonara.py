from flask import *

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('say.html')

@app.route('/acharamor', methods=['post'])
def verificar_amado():
    nome_pessoa = request.form.get('candidato')

    return render_template('elaquervc.html')
    #return render_template('elanaoquervc.html')

if __name__ == '__main__':
    app.run()