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
def notas(*nota,situação=False):
    """
    -> Função Para Analisar Notas E Situações De Vários Alunos.
    :param nota:Uma ou mais notas dos alunos (aceita várias)
    :param situação:Valor opcional, indicando se deve ou não adicionar a situação 
    :return: Dicionário com váriasinformações sobre a situação da turma.
    """
    resultado = dict()
    resultado['total'] = len(nota)
    resultado['maior'] = max(nota)
    resultado['menor'] = min(nota)
    resultado['média'] = sum(nota)/len(nota)
    if situação:
        if resultado['média'] >= 7:
            resultado['situação'] = 'Isto ai, continue estudando sempre.'
        elif resultado['média'] >= 5:
            resultado['situação'] = 'Dá Pra Passar.'
        else:
            resultado['situação'] = 'Me ajuda a te ajuda, estude.'
    return resultado 
# Programa Principal 
resposta = notas(5.5, 2.5, 9, 8.5, situação=True)
help(notas)
