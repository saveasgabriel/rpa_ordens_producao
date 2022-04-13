import pyautogui as rpa #Biblioteca para manipulacao de mouse, tela e teclado
import pygetwindow as win #Bibliotecas para manipulacao de janelas
import time
import ativar_janela

def aguardarJanelaPorNome(nomeJanela):
    time.sleep(1)
    condicao = 0;
    win.getWindowsWithTitle(nomeJanela)
    
    while condicao == 0:   
        window = rpa.getWindowsWithTitle(nomeJanela)
        if window != []:
            #print('Achou a janela AUTENTICAÇÃO!', window)
            condicao = 1
        else:
            condicao = 0
            #print('Não achou a janela AUTENTICAÇÃO!')
    else:
        #Ativar tela do ERP
        ativar_janela.ativarJanela(nomeJanela)