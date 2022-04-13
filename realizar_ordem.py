import aguardar_janela_imagem as aguardarImg
import config
import login_ERP
import fechar_janelas_ERP as fecharWin
import abrir_janela_ERP as abrirWin
import incluir_parametros_cfbpd266 as cfbpd266 
import pyautogui as rpa
import fracionar_plano_ERP as fracionar
import buscar_novo_cod_ERP as buscarCod
import taskkill_janela as taskkill

login_ERP.fazerLogin(config.caminhoERP, config.nomeUser, config.senhaUser,
                     config.janelaAutenticacao, config.janelaERPCorporate,
                     config.genericosERPDireto+"Mensagem_Abertura_ERP.jpg")

fecharWin.fecharJanelaERP(config.janelaERPCorporate)

abrirWin.abrirJanelaERP(config.planejamentoProdPeriodo, config.CFBPD266Direto+"CodigoTela_CFBPD266_ERP.jpg", 
                        config.janelaERPCorporate)

#INCLUIR DATA, COD UNIDADE, TIPO DE PRODUCAO E ESTRUTURA NO PLANEJAMENTO POR PERIODO INICIAL
cfbpd266.incluirParametro(config.janelaERPCorporate, 121, 157, 22, config.janelaCFBPD266A, 
                          config.CFBPD266Direto+"CodigoSubTela_CFBPD266A_ERP.jpg", 2, 'left', 
                          ['13042022', '70', '552', '10'], 'press', 'f3', '', '')

#ABRIR TELA DE PRE ORDEM
rpa.hotkey('ctrl', 's'); aguardarImg.aguardarJanelaPorImagem(config.CFBPD266Direto+"CodigoSubTela_CFBPD266B_ERP.jpg",
                                                 config.janelaCFBPD266B)

#INCLUIR DATA PRE ORDEM
cfbpd266.incluirParametro(config.janelaERPCorporate, 470, 149, 22, '', 
                         '', 2, 'left', ['13042022'], '', '', '', '')

#INCLUIR LINHA, DESCRICAO, QTD PREVISTO E PESO NA PRE ORDEM
cfbpd266.incluirParametro(config.janelaERPCorporate, 470, 194, 22, '', 
                         '', 2, 'left', ['1', 'VIA RPA', '300', '300'], '', '', '','')

#INCLUIR HABILITAÇÃO NA ENTRADA
cfbpd266.incluirParametro(config.janelaERPCorporate, 345, 364, 22, '', 
                         '', 2, 'left',['1', '45', '110', '2'],'', '', 'true', 2)

#INCLUIR PRODUTO DE ENTRADA
cfbpd266.incluirParametro(config.janelaERPCorporate, 345, 501, 22, config.janelaCFBPD266A, 
                         config.CFBPD266Direto+"GridHabilitacao_CFBPD266A_ERP.jpg", 2, 'left', 
                         ['374155'], 'press', 'f4', '', '')

#FRACIONAR E GRAVAR ORDEM
fracionar.fracionarPlano(57, 184, 1, 'left', config.janelaCFBPD266A, 
                         config.CFBPD266Direto+"CodigoTela_CFBPD266_ERP.jpg", config.janelaERPCorporate)

#BUSCAR COD DA ORDEM GERADA
novo_cod = buscarCod.returnNovoCodOrdem(686, 183, 2, 'left', config.janelaERPCorporate, 
                             config.CFBPD266Direto+"CodigoTela_CFBPD266_ERP.jpg",
                             config.janelaCFBPD266A, config.CFBPD266Direto+"CodigoSubTela_CFBPD266A_ERP.jpg")

#FECHAR O ERP
taskkill.close(config.fecharCorporate, config.cmd)







