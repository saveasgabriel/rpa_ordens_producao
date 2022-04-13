import pyautogui as rpa
import mouse_click as mouse
import time
import aguardar_janela_imagem as aguardar

def fracionarPlano(x, y, qtdClick, botaoMouse, nomeJanelaAtual, imagemJanelaAguardar, nomeJanelaAguardar):
     
    time.sleep(1)
    mouse.clicar(x, y, qtdClick, botaoMouse, 
        nomeJanelaAtual)

    #ATUALIZAR SALDO
    rpa.hotkey('ctrl','alt','p')
    time.sleep(1)
    rpa.press('enter')

    time.sleep(1)

    #FRACIONAR PLANO NÃO CORINGA
    rpa.hotkey('ctrl','alt','a')
    time.sleep(1)
    rpa.press('enter')
    
    #GRAVAR
    rpa.press('f4')
    
    aguardar.aguardarJanelaPorImagem(imagemJanelaAguardar, nomeJanelaAguardar)
    
    


