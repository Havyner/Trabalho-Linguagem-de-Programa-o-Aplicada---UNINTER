# Importando a biblioteca
import pygame as pg

from code.menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT

class Game:
    def __init__(self):
        # Iniciando o pygame
        pg.init()
        # Abrindo uma janela
        self.window = pg.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass