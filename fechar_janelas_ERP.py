import pyautogui as rpa #Biblioteca para manipulacao de mouse, tela e teclado
import time
import ativar_janela

def fecharJanelaERP(nomeJanela):
    time.sleep(1)
    ativar_janela.ativarJanela(nomeJanela)
    rpa.hotkey('alt', 'f10')
    rpa.press('tab')
    rpa.press('enter')
