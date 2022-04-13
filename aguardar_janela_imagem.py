import pyautogui as rpa #Biblioteca para manipulacao de mouse, tela e teclado
import pygetwindow as win #Bibliotecas para manipulacao de janelas
import time
import ativar_janela
import mouse_click as click

#from logging import exception
import cv2 as i #Biblioteca para manipulações de imagens

def aguardarJanelaPorImagem(diretorioImagem, nomeJanela, clickImagem='false'):
    time.sleep(1)
    condicao = 0 
    while condicao == 0:
        localImagem = rpa.locateOnScreen(diretorioImagem, confidence = 0.9)
        #print(localImagem)
        try:
            localImagemPoint = rpa.center(localImagem)
        except:
            print('Janela não está aberta!')
            condicao = 0
        else:
            condicao = 1
            print('Janela está aberta!')
    print(localImagemPoint, localImagemPoint)
       
    ativar_janela.ativarJanela(nomeJanela)
       
    if clickImagem == 'true':
        clicarImagem(localImagemPoint, 1, 'left', nomeJanela)
        print(localImagemPoint, localImagemPoint)
        
    
    
def clicarImagem(localImagemPoint, qtdClick, botaoMouse, nomeJanela):
    click.clicar(localImagemPoint[0], localImagemPoint[1],qtdClick, botaoMouse, nomeJanela)