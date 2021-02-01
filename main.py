import PySimpleGUI as sg

class TelaPrincipal:
    def __init__(self):
        # LAYOUT DA TELA
        layout = [
            # BARRA
            [sg.Image(filename=('_img/fgts-o-saque.png'),
                      background_color=None,
                      size=(300, 100),
                      )
             ],
            # ELEMENTOS TEXTO E ENTRADA
            [sg.Text('Anos de Empresa : ', 
                     size=(10, 0),
                     font=20),

             sg.Input(size=(20, 5), key='work_time')],

            [sg.Text('Seu Salário : ',
                     size=(10, 0),
                     font=20),

             sg.Input(size=(20, 5), key='work_money')],

            # BOTÕES
            [sg.Button('Calcular',), sg.Button('Sair')],
            [sg.Text('versão: 0.1', text_color='red')],

            # SAÍDA
            [sg.Output(size=(300, 400))]
        ]

        self.window = sg.Window('Calculo FGTS',
                                layout,
                                font=('Segoe UI', 12),
                                size=(300, 450)
                                )

    def run(self):

        # LOOP TELA
        while True:
            self.event, self.values = self.window.read()

            # EXTRAÇÃO DE VALORES
            work_time = float(self.values['work_time'])
            work_money = int(self.values['work_money'])
            # CÁLCULOS
            calculo_meses = work_time * 12
            taxa_fgts = work_money * 0.08
            fgts_total = calculo_meses * taxa_fgts
            taxa_multa = fgts_total * 0.4
            valor_aproximado = fgts_total + taxa_multa
            # IMPRESSÃO DE DADOS
            print(f'\nSALDO FGTS ACUMULADO \n R$: {fgts_total:.2f}\n')
            print(f'VALOR FGTS + MULTA\n R$: {valor_aproximado:.2f}\n')

            if self.event == sg.WIN_CLOSED or self.event == 'Sair':
                break

        # ENCERRA O PROGRAMA
        self.window.close()


# INICIALIZA APLICAÇÃO
tela = TelaPrincipal()
tela.run()
