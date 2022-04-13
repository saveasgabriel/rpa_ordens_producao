import pyautogui as rpa
import aguardar_janela_nome as janelaNome
import ativar_janela as ativar
import mouse_click as click
import time 
import aguardar_janela_imagem as janelaImagem
import copiar_area_transferencia as copy

def returnNovoCodOrdem(x, y, qtdQlick, botaoMouse, nomeJanela, atualJanelaImagem, aguardarJanelaNome, aguardarJanelaImagem):
    ativar.ativarJanela(nomeJanela)
    rpa.press('f3')
    janelaImagem.aguardarJanelaPorImagem(aguardarJanelaImagem, aguardarJanelaNome)
    click.clicar(x, y, qtdQlick, botaoMouse, aguardarJanelaNome)
    rpa.hotkey('ctrl', 'c')
    time.sleep(1)
    
    novaOrdemGerada = copy.copiar()
    
    rpa.press('f4')
    janelaImagem.aguardarJanelaPorImagem(atualJanelaImagem, nomeJanela)
    
    return novaOrdemGerada
    
