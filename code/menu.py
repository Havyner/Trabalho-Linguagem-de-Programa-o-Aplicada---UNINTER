import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

class Menu:
    def __init__(self, window):
        self.window = window
        # Imagem do Menu
        self.surf = pg.image.load('./asset/menu.png')
        # Criando um retângulo para colocar a imagem dentro
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        # Música do menu
        pg.mixer_music.load('./asset/sound/menu.wav')
        pg.mixer_music.play(-1) # -1 para manter ela em loop

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pg.display.flip()

            # Mantendo a janela aberta
            # iniciando os eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit() # Fechar a janela
                    quit() # Finalizando a pygame
    
    # Criando o texto
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Comic Sans", size=text_size)
        text_surf: Surface = text_font.render(text, antialias:True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        