# Janelas para pedidos

from PySimpleGUI import PySimpleGUI as sg

# Criar as janeleas e estilos(layout)


def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input('')],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)


def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Pepperoni', key='pizza1'), sg.Checkbox(
            'Pizza Frango c/ Catupiry', key='pizza2')]
    ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)


# Criar as janelas iniciais
janela1, janela2 = janela_login(), None
# Criar um loop de leitira de eventos
while True:
    window, event, values = sg.read_all_windows()
    # Quando janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    # Quando queremos ir para próxima janela
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()

    # Quando queremos voltar para janela anterior
# Lógica de  o que deve conectar ao clicar os botões