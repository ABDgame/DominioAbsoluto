'''
    Melhore o DESAFIO 052, perguntando 
para o usuário se ele quer mostrar 
mais alguns termos. O programa
encerrará quando ele disser que quer
mostrar 0 termos.

'''
print('○●' * 20)
print('Gerador de PA')
print('●○' * 20)
primeiro = int(input('Primeiro termo: '))  
razão = int(input('Razão da PA: '))
termo = primeiro 
cont = 1
total = 0
mais = 10
while mais != 0:
   total = total + mais
   while cont <= total:
       print('{} -> '.format(termo), end='')
       termo += razão 
       cont += 1
   print('PAUSA')
   mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finaliza com {} termos mostrados.'.format(total))
   
