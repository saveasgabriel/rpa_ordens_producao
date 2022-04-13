import pyautogui as rpa
import mouse_click as mouse
import time
import aguardar_janela_imagem as aguardar
import incluir_parametros_cfbpd266 as parametrizar
import config

def fracionarPlanoSimples(x, y, qtdClick, botaoMouse, nomeJanelaAtual, imagemJanelaAguardar, nomeJanelaAguardar):
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


def fracionarPlanoFiltro(xfamilia, yfamilia, 
                         xrendFamilia, yrendFamilia, 
                         xfiltro, yfiltro, 
                         xsaidaProd, ysaidaPrd,  
                         qtdClick, botaoMouse, 
                         imagemJanela, 
                         imagemJanelaFamilia, 
                         imagemJanelaRendFamilia,
                         imagemJanelaFiltro,
                         imagemConfirmar,
                         imagemJanelaERP,
                         nomeJanelaERP,
                         nomeJanela, 
                         nomeJanelaFiltro,
                         filtro, 
                         vezesDirecao, loopInclusao):
    
    filtroColunaFamilia(imagemJanelaFamilia, nomeJanela, xfamilia, yfamilia, qtdClick, botaoMouse, 
                        ['igual a', filtro[0][0]], imagemJanela,
                        nomeJanelaFiltro, xfiltro, yfiltro, imagemJanelaFiltro, vezesDirecao, imagemConfirmar)
    
    filtroColunaRendSubFamilia(imagemJanelaRendFamilia, nomeJanela, xrendFamilia, yrendFamilia, qtdClick, botaoMouse, 
                               ['igual a', filtro[0][1]], imagemJanela,
                               nomeJanelaFiltro, xfiltro, yfiltro, imagemJanelaFiltro, vezesDirecao, imagemConfirmar)
    
    incluirCodSaida(xsaidaProd, ysaidaPrd, qtdClick, botaoMouse, nomeJanela, loopInclusao,
                    imagemJanelaERP, nomeJanelaERP)


def filtroColunaFamilia(imagemJanelaFamilia, nomeJanela, xfamilia, yfamilia, qtdClick, botaoMouse,
                        pesquisa, imagemJanela,
                        nomeJanelaFiltro, xfiltro, yfiltro, imagemJanelaFiltro, vezesDirecao, imagemConfirmar):
    
    aguardar.aguardarJanelaPorImagem(imagemJanelaFamilia, nomeJanela, 'true')
    
    mouse.clicar(xfamilia, yfamilia, qtdClick, botaoMouse, nomeJanela)
    
    aguardar.aguardarJanelaPorImagem(imagemJanela, nomeJanela, 'true')
    
    parametrizar.incluirParametro(nomeJanelaFiltro, xfiltro, yfiltro, 0, '', imagemJanelaFiltro, qtdClick, botaoMouse, 
                                  pesquisa, '', '', 'true', vezesDirecao)
    
    aguardar.aguardarJanelaPorImagem(imagemConfirmar, nomeJanelaFiltro, 'true')
    
    
def filtroColunaRendSubFamilia(imagemJanelaRendFamilia, nomeJanela, xrendFamilia, yrendFamilia, qtdClick, botaoMouse,
                               pesquisa, imagemJanela,
                        nomeJanelaFiltro, xfiltro, yfiltro, imagemJanelaFiltro, vezesDirecao, imagemConfirmar):
    aguardar.aguardarJanelaPorImagem(imagemJanelaRendFamilia, nomeJanela, 'true')
    
    mouse.clicar(xrendFamilia, yrendFamilia, qtdClick, botaoMouse, nomeJanela)
    
    aguardar.aguardarJanelaPorImagem(imagemJanela, nomeJanela, 'true')
    
    parametrizar.incluirParametro(nomeJanelaFiltro, xfiltro, yfiltro, 0, '', imagemJanelaFiltro, qtdClick, botaoMouse, 
                                  pesquisa, '', '', 'true', vezesDirecao)
    
    aguardar.aguardarJanelaPorImagem(imagemConfirmar, nomeJanelaFiltro, 'true')
    

def incluirCodSaida(xsaidaProd, ysaidaPrd, qtdClick, botaoMouse, nomeJanela, loopInclusao,
                    imagemJanelaERP, nomeJanelaERP):
    i = 0
    mouse.clicar(xsaidaProd, ysaidaPrd, qtdClick, botaoMouse, nomeJanela)
    while i <= loopInclusao:
        i = i+1
        rpa.write('1')
        time.sleep(0.5)
        rpa.press('down')
        
    rpa.press('f4')
    
    aguardar.aguardarJanelaPorImagem(imagemJanelaERP, nomeJanelaERP)
     