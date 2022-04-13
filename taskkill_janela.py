import pyautogui as rpa
import aguardar_janela_nome as aguardar

def close(comando, aguardarJanela):
    rpa.hotkey('win', 'r')
    rpa.write('cmd')
    rpa.press('enter')
    aguardar.aguardarJanelaPorNome(aguardarJanela)
    rpa.write(comando)
    rpa.press('enter')
    rpa.write('taskkill /im cmd.exe')
    rpa.press('enter')
    