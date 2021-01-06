'''
    Desafio #040 - Aquele clássico da Média 
Crie um programa que leia duas notas de um aluno e calcule sua média.
Mostre uma mensagem no final, de acordo  com a média atingida.
 - Média abaixa de 5.0: Reprovado
 - Média entre 5.0 e 6.9 : Recuperação 
 - Média 7.0 ou superior : Aprovado
'''
print('-='*20)
print('         Média Entre Duas Notas')
print('-='*20)
while True:
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    média = (nota1 + nota2) / 2
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
    if 7 > média >= 5:
        print('O aluno está em Recuperação ')
    elif média < 5:
        print ('Aluno está Reprovado. ')
    elif média >= 7:
        print ('O aluno está Aprovado.')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Calcular Outras Notas ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('::'*20)
print('       Pausa Para O Café ')
print('::'*20)
        
