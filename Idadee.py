import PySimpleGUI as sg

class TelaIdade:
    def __init__(self):
        layout = [
            [sg.Text('Insira o seu Nome', size=(15, 0)), sg.Input(size=(15, 0), key='nome')],
            [sg.Text('Insira a sua Idade', size=(15, 0)), sg.Input(size=(15, 0), key='idade')],
            [sg.Button('CLIQUE AQUI',)],
            [sg.Output(size=(35,10))]
        ]

        self.janela = sg.Window('Dados do Usuario').layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = int(self.values['idade'])
            print('Nome: {}\nIdade: {}'.format(nome, idade))

            if idade > 0 and idade < 18:
                print(nome,'é uma crianca.')
            else:

                if idade >= 18 and idade < 35:
                    print(nome,'é jovem.\n')
                else:

                    if idade >= 35 and idade < 60:
                        print(nome,'é adulto.\n')
                    else:

                        if idade >= 60 and idade < 125:
                            print(nome,'é idoso.\n')
                        else:
                            print('Idade Invalida.\n')


tela = TelaIdade()
tela.Iniciar()

