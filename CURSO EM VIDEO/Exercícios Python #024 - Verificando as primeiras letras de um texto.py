# Crie um programa que leia o nome de uma cidade e diga se ela
# começa ou não com o nome "CURITIBA".
cidade = str(input('Em que cidade você nasceu?')).strip()
print(cidade[:8].upper()== 'CURITIBA')