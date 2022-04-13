import pyautogui as rpa #Biblioteca para manipulacao de mouse, tela e teclado
import pygetwindow as win #Bibliotecas para manipulacao de janelas

def ativarJanela(nomeJanela):
        print(nomeJanela)
        window = rpa.getWindowsWithTitle(nomeJanela)[0]
        window.activate()