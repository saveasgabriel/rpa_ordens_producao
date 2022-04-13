from ast import Import; import pyautogui as rpa; 
import aguardar_janela_imagem as aguardar; import mouse_click as click

"""Comment
janelaClick -> em qual janela será inserido os parâmetros
qtdClick -> quantos clicks em cada campo
x, y -> localização do click mouse
botaoMouse -> qual botao do mouse clicar ('left', 'right', 'midle')
rangeParametros -> os parametros a serem usados
aumentoCampo -> a cada parametros inserido o será incrementado um valor em y para progredir nos campos 
tipoOpClick -> depois de inserido todos os parametros, sera usado um tipo de comando (press, write ou hotkey)
    se colocar 'nao', então não fará nenhum tipo de operacao
operacaoClick -> o comando a ser usado no tipo tipoOpClick (ex: ('ctrl', 's'), 'f4')
nomeJanelaA -> nome de janela a ser aguardada após operação final
janelaImagemA -> após operacao fnal, aguardar por imagem, e assim identificar se janela entrou
botaDirecao - caso opite por navegar entre os campos por 'tab', então deixar como 'true'
vezesDirecao - se navegar por 'tab', coloque quantas vezes será pressionado a tecla até chegar 
    ao próximo campo
"""

def incluirParametro(janelaClick, x, y, aumentoCampo, nomeJanela, janelaImagem, qtdClick, 
                      botaoMouse, rangeParametros, tipoOpClick, operacaoClick, botaDirecao, vezesDirecao):
    #DESLOCAR MOUSE PARA TIRAR SELEÇÃO ATUAL 
    click.clicar(x, y+aumentoCampo, qtdClick, botaoMouse, janelaClick)
    
    #INSERIR PARÂMETROS
    cont = 0
    for indice in range(len(rangeParametros)):
        #print(f"RangeParametros - {rangeParametros[indice]}")
        if cont == 0:
            click.clicar(x, y, qtdClick, botaoMouse, janelaClick)
        rpa.write(rangeParametros[indice])
        
        i = 0 
        #SE O MOVIMENTO FOR POR TAB E NÃO POR MOUSE CLICK
        if botaDirecao == 'true':
            while i < vezesDirecao:
                rpa.press('tab')
                cont = cont + 1
                i = i + 1
           
        y = y + aumentoCampo
        
    #CARREGAR ALGO APÓS INSERIR PARÂMETROS (JANELAS)  
    operacaoFinal(nomeJanela, janelaImagem, tipoOpClick, operacaoClick)    
    
def operacaoFinal(nomeJanelaA, janelaImagemA, tipoOpClick, operacaoClick):
    if tipoOpClick != '':
        if tipoOpClick == 'press':
            rpa.press(operacaoClick)

        elif tipoOpClick == 'hotkey':
            rpa.hotkey(operacaoClick) 

        elif tipoOpClick == 'write':
            rpa.write(operacaoClick)

        aguardar.aguardarJanelaPorImagem(janelaImagemA, nomeJanelaA)
