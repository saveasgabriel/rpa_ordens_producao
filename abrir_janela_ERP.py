import pyautogui as rpa #Biblioteca para manipulacao de mouse, tela e teclado
import time
import aguardar_janela_imagem as aguardar

def abrirJanelaERP(codTelaERP, imagemjanela, nomeJanela):
    time.sleep(1)
    rpa.hotkey('alt', 'f2')
    rpa.write(codTelaERP)
    rpa.press('enter')
    
    aguardar.aguardarJanelaPorImagem(imagemjanela, nomeJanela)
    