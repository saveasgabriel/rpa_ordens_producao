#CONEXAO BD_POSTGRES
host = 'localhost'
dbname = 'postgres'
user = 'postgres'
password = '1234'
sslmode = 'prefer'

#USUARIO ERP
senhaUser = 'W7g3k9a5%'
nomeUser = 'gabrielfranca-pdp'

#DIRETÓRIOS
caminhoERP = "K:\\Div\\CorporateUpdater\\JBS.Updater.Corporate.exe"
caminhoPastasImagens = "C:\\Users\\gabrielfranca-pdp\\Desktop\\RPA_ReconheicmentoImagem_Python\\"
pastaImagens_Raiz_trajetos_ERP = "Raiz_trajetos_ERP\\"
pastaImagensGenericos_ERP = "Genericos_ERP\\"
pastaImagensCFBPD266_ERP = "CFBPD266_planejamentoPorPeriodo_ERP\\"

#DIRETÓRIOS AGRUPADOS
genericosERPDireto = caminhoPastasImagens + pastaImagensGenericos_ERP; #CAMINHO DIRETO Genericos_ERP\\
CFBPD266Direto = caminhoPastasImagens + pastaImagensCFBPD266_ERP; #CAMINHO DIRETO PARA A IMAGENS DA TELA CFBPD266   

#NOMES JANELAS
janelaAutenticacao = 'Autenticação'
janelaERPCorporate = 'Corporate (PDP JBS)' #POSTERIORMENTE O '*' SERÁ TROCADO POR ALGUMA SIGLA
janelaCFBPD266A = 'Planejamento de Produção por Período' #JNAELA DERIVADA DA PLANEJAMENTO DE PRODUÇÃOPOR PERIODO CFBPD266
janelaCFBPD266B = 'Pré-Ordem de Produção' #JNAELA DERIVADA DA PLANEJAMENTO DE PRODUÇÃOPOR PERIODO CFBPD266
cmd = 'C:\\Windows\\system32\\cmd.exe'
janelaCFBPD266A_Filtro = 'Filtro Automático Personalizado'

#CODIGOS JANELAS ERP
planejamentoProdPeriodo = 'cFBPD266'

#COMANDOS TASKKILL
fecharCorporate = 'taskkill /im corporate*'

#PASTA COMUNS
folderComuns = 'C:\\Users\gabrielfranca-pdp\\Documents\Repositorios_github\\projetos_python\RPA\Comuns\\'