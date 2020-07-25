import PySimpleGUI as bm

class TelaSoma:
    def __init__(self):
        layout = [
            [bm.Text('Insira os valores do primeiro vector')],
            [bm.Text('1'), bm.Input(size=(5,0), key='v1'), bm.Text('2'), bm.Input(size=(5,0),key='v2'), bm.Text('3'), bm.Input(size=(5,0),key='v3')],
            [bm.Text('Insira os valores do segundo vector')],
            [bm.Text('1'), bm.Input(size=(5,0),key='v4'), bm.Text('2'), bm.Input(size=(5,0),key='v5'), bm.Text('3'), bm.Input(size=(5,0),key='v6')],
            [bm.Button('CALCULAR')],
            [bm.Output(size=(30,10))]
        ]

        self.janela = bm.Window('SOMA VECTOR').layout(layout)


    def Iniciar(self,):
        while True:
            self.button, self.values = self.janela.Read()
            v1 = int(self.values['v1'])
            v2 = int(self.values['v2'])
            v3 = int(self.values['v3'])
            v4 = int(self.values['v4'])
            v5 = int(self.values['v5'])
            v6 = int(self.values['v6'])

            vetor = [v1, v2, v3]
            vetor1 = [v4, v5, v6]
            S = [0, 0, 0]

            print("O primeiro vector é:")
            for i in range(0, 1):
                print(vetor, end="  ")

            print("\n")

            print("O segundo vector é:")
            for i in range(0, 1):
                print(vetor1, end="  ")

            print("\n")

            for i in range(0, 1):
                S = vetor1 + vetor

            print("O vector soma é:")
            for i in range(0, 1):
                print(S, end="  ")

tela = TelaSoma()
tela.Iniciar()
