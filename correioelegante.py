from flask import *

app = Flask(__name__)

@app.route('/')
def pag_principal():
    return render_template('correioelegante.html')

@app.route('/registrar', methods=['POST'])
def registrar_valor():
    nome = request.form.get('pagante')
    valor = request.form.get('valor')

    arquivo = open('registro.txt','a')
    linha = f'{nome}-{valor}\n'
    arquivo.write(linha)
    arquivo.close()
    return render_template('correioelegante.html')

@app.route('/computartotal')
def computar_valor():
    arquivo = open('registro.txt', 'r')
    linhas = arquivo.readlines()
    soma = 0
    for linha in linhas:
        valor = linha.split('-')[1]
        valor = valor.replace('\n','')
        valor = int(valor)
        soma += valor

    arquivo.close()
    return f'os professores pagaram no total {soma} reais'

if __name__ == '__main__':
    app.run()