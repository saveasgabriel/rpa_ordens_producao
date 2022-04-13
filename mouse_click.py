import pyautogui as rpa
import time
import aguardar_janela_nome as aguardar

#left - esquerdo
#midle - meio
#right - direito
def clicar(x, y, qtdClick, botaoMouse, nomeJanela):
    
    aguardar.aguardarJanelaPorNome(nomeJanela)
    
    time.sleep(1)
    
    rpa.click(x, y, clicks=qtdClick, button=botaoMouse)

    
