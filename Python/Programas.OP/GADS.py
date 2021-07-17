import random
import PySimpleGUI as sg
import os
from playsound import playsound

class GADS:
    def __init__(self):
        sg.theme('Reds')
        #playsound('Macha_Imperial.mp3', block=False)
        layout = [
            [sg.Text('Site / Programa', size=(12, 1)), sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail / Usuário', size=(12, 1)), sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'),sg.Combo(values=list(range(26)),key='QCaracteres',default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar senha')]
        ]
# A janela
        self.janela = sg.Window('GADS', layout)

    def Iniciar(self):
        while True:
            evento, valores= self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)
# Randomizador
    def gerar_senha(self, valores):
        #Char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÇç1234567890!@#$%&*?'
        #chars = random.choices(Char_list, k=int(valores['QCaracteres']))
        E1List = 'EPWAepwa37421Æ!?#'
        chars = random.choices(E1List, k=int(valores['QCaracteres']))
        new_pass = ''.join(chars)
        return new_pass
    
    def salvar_senha(self, nova_senha,valores):
        with open('Gads.txt','a',newline='') as arquivo:
            arquivo.write(f" Site: {valores['site']}, Usuario: {valores['usuario']}, Senha: {nova_senha}\n")
        print('Arquivo salvo')

gen = GADS()
gen.Iniciar()