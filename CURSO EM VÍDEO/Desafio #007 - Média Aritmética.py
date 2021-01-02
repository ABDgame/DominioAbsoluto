'''
   Desafio 007 - Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua média.   
'''
while True:
    aluno = str(input('Digite o nome do(a) aluno(a):  '))
    n1 = float(input ('Digite a primeira nota:  '))
    n2 = float(input('Digite a segunda nota:  '))
    n3 = float(input ('Digite a terceira nota:  '))
    n4 = float(input ('Digite a quarta nota:  '))
    mediabi = (n1+n2+n3+n4)/4
    print ('A media do(a) aluno(a) {} é:{:.1f} '.format(aluno, mediabi))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Calcular E Mostrar Outra Média ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café !!!')    
