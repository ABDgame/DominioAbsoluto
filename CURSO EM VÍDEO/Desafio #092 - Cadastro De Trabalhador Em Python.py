'''
     Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-os (com idade) em um dicionário se por
acaso a CTPS for diferente de ZERO, o dicionário receberá 
também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos e pessoa vai se aponsentar.
       
         
'''
from datetime import datetime
dados = dict()
while True:
    dados['nome'] = str(input('Nome: '))
    nascimento = int(input('Ano De Nascimento: '))
    dados['idade'] = datetime.now().year - nascimento
    dados['ctps']= int(input('Carteira De Trabalho (0 não tem): '))
    if dados['ctps'] != 0:
        dados['contratação'] = int(input('Ano De Contratação: '))
        dados['salário'] = float(input('Salário: R$ '))
        dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
    print('-=' * 30)    
    for chave, valor in dados.items():
        print(f'  - {chave} : {valor}')         
    resposta = str(input('Deseja Cadastrar Outro Trabalhador? [S/N]'))
    if resposta in 'Nn':
        break
print('-='*20)
print('       Pausa Para O Café ')
print('-='*20)
     
    

    


         

