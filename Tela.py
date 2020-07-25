import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Nome', size=(5, 0)), sg.Input(size=(15, 0), key='nome')],
            [sg.Text('Idade', size=(5, 0)), sg.Input(size=(15, 0), key='idade')],
            [sg.Text('Que tipo de contas sao aceitas?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Button('OK')],
            [sg.Output(size=(30,10))]
        ]

        self.janela = sg.Window("Dados do Usuario").layout(layout)



    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            gmail = self.values['gmail']
            yahoo = self.values['yahoo']
            print('Nome: {}\nIdade: {}\nGmail: {}\nYahoo: {}\n'.format(nome, idade, gmail, yahoo))


tela = TelaPython()
tela.Iniciar()
