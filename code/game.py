# Importando a biblioteca
import pygame as pg

from code.menu import Menu

class Game:
    def __init__(self):
        # Iniciando o pygame
        pg.init()
        # Abrindo uma janela
        self.window = pg.display.set_mode(size = (600, 480))


    def run(self, ):
        while True:
            menu = menu(self.window)
            menu.run(self, )
            pass



        '''
        # Mantendo a janela aberta
        while True:
            # iniciando os eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit() # Fechar a janela
                    quit() # Finalizando a pygame
        '''