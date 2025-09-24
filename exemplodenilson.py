filmes = [['nome filme','genero',[['19','21'],['16','22'],['19','20'],['19','22'],['19','21']]]]


nome_filme = input('qual filme voce quer assistir')
dia = input('qual dia da semana vc quer ver os horarios')

if dia == 'segunda':
    d = 0
elif dia == 'terca':
    d = 1
elif dia == 'quarta':
    d = 2

for f in filmes:
    if f[0] == nome_filme:
        for horario in f[2][d]:
            print('-------')
            print(horario)
