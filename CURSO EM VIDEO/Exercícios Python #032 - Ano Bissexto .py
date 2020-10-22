# Exercício Python 032 - Ano Bissexto
from datetime import date
ano = int(input('Qual ano você quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
     print('O ano {} é Bissexto '.format(ano))
else:
     print ('O ano {} Não é Bissexto '.format(ano))