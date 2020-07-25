import PySimpleGUI as bb

class TelaPrimo:

    def __init__(self):
        layout = [
            [bb.Text('Insira o primeiro valor', size=(18, 0)), bb.Input(size=(30, 0), key='num1')],
            [bb.Text('Insira o segundo valor', size=(18, 0)), bb.Input(size=(30, 0), key='num2')],
            [bb.Button('CLIQUE AQUI PARA VERIFICAR')],
            [bb.Output(size=(50,15))]
        ]

        self.janela = bb.Window('Numeros Primos').layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            a = int(self.values['num1'])
            b = int(self.values['num2'])
            quant = list()

            if a >= 5 and a <= 999 and b >= 5 and b <= 999:
                if a > b:
                    for i in range(b, a + 1):
                        cont = 0
                        j = 0
                        while (j <= i):
                            j = j + 1
                            if i % j == 0:
                                cont = cont + 1
                        if cont == 2:
                            quant = quant + 1

                    print("Os numeros primos que existem no intercalo de [{}-{}] sao:\n{}".format(b, a, quant))
                else:
                    for i in range(a, b + 1):
                        cont = 0
                        j = 0
                        while (j <= i):
                            j = j + 1
                            if i % j == 0:
                                cont = cont + 1
                        if cont == 2:
                            quant.append(i)

                    print("Os numeros primos que existem no intercalo de [{}-{}] sao:\n{}\n".format(a, b, quant))

        else:
            lb3["text"] = "nao pessivel verificar"


tela = TelaPrimo()
tela.Iniciar()
