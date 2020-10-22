# Desafio 011
largura = float(input('Largura da Parede '))
altura = float(input (' Altura da Parede '))
área = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de{}m2'.format(largura, altura, área))
tinta = área / 2
print ('Para pintar essa parede, você precisará de {}L de tinta'.format(tinta))