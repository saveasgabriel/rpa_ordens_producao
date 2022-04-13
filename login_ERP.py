import pyautogui as rpa
import aguardar_janela_nome as aguardar
import aguardar_janela_imagem as aguardarImg
import time

def fazerLogin(caminhoERP, usuario, senha, janelaAutenticacao,janelaERPCorporate, caminhoImagemJanela):
    time.sleep(1)
    rpa.hotkey('win', 'r'); rpa.write(caminhoERP); rpa.press('enter')  
    
    aguardar.aguardarJanelaPorNome(janelaAutenticacao)
    
    #Incluir senha de user
    window = rpa.getWindowsWithTitle('Autenticação')[0]; window.activate()
    rpa.hotkey('shift', 'tab');rpa.write(usuario);rpa.press('tab')
    rpa.write(senha);rpa.press('tab');rpa.write('pdp');rpa.press('enter')
    rpa.press('tab');rpa.press('enter')
    
    #Aguardar janela base entrar 
    aguardar.aguardarJanelaPorNome(janelaERPCorporate)
    aguardarImg.aguardarJanelaPorImagem(caminhoImagemJanela, janelaERPCorporate)

        