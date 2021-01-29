'''
    Faça um programa que tenha uma
função notas() que pode receber
várias notas de alunos e vai retornar 
um dicionário com as seguintes
informações:
    - Quantidade de Notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)
    Adicione também as docstrings.
'''
def notas(*nota, situação=False):
    resultado = dict()
    resultado['total'] = len(nota)
    resultado['maior'] = max(nota)
    resultado['menor'] = min(nota)
    resultado['média'] = sub()
# Programa Principal 
resposta = notas(5.5, 2.5, 9, 8.5)
print(resposta)
