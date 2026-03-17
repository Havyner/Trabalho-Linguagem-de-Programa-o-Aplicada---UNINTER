import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font
from code.const import WIN_WIDTH, COLOR_WHITE, COLOR_BLACK, COLOR_GREEN, MENU_OPTION

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
            # Texto do menu
            self.menu_text(20, text="Havyner Siqueira RU: 5079616", text_color=COLOR_GREEN, text_center_pos=((WIN_WIDTH / 2), 20))
            self.menu_text(70, text="KILL ZUMBIES", text_color=COLOR_BLACK, text_center_pos=((WIN_WIDTH / 2), 80))

            for i in range(len(MENU_OPTION)):
                self.menu_text(40, text=MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=((WIN_WIDTH / 2), 230 + 50 * i))


            pg.display.flip()

            # Mantendo a janela aberta
            # iniciando os eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit() # Fechar a janela
                    quit() # Finalizando a pygame
    
    # Criando o texto
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Arial Black", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        